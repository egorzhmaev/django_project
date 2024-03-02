from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from women.models import translit_to_eng
from django.urls import reverse
from django.utils import timezone
from django.core.cache import cache

class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография", default="default.png")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.username))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:show_profile', kwargs={'slug': self.slug})

    def is_online(self):
        last_seen = cache.get(f'last-seen-{self.id}')
        if last_seen is not None and timezone.now() < last_seen + timezone.timedelta(seconds=300):
            return True
        return False