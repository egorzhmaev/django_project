from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages
from women.models import ViewCount

menu = [{'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
]

class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by = 3

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected
    def get_mixin_context(self,context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context

def get_client_ip(request):
    """
    Получаем IP
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip

class ViewCountMixin:
    """
    Миксин для увеличения счетчика просмотров статьи
    """
    def get_object(self):
        # получаем статью из метода родительского класса
        obj = super().get_object()
        # получаем IP-адрес пользователя
        ip_address = get_client_ip(self.request)
        # получаем или создаем запись о просмотре статьи для данного пользователя
        ViewCount.objects.get_or_create(women=obj, ip_address=ip_address)
        return obj


class UserIsNotAuthenticated(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_authenticated:
            messages.info(self.request, 'Вы уже авторизованы. Вы не можете посетить эту страницу.')
            raise PermissionDenied
        return True

    def handle_no_permission(self):
        return redirect('home')