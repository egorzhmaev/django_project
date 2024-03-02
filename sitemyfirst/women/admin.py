from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from .models import Women, Category, Comment, Feedback, ViewCount


# Register your models here.
@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    pass

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'ip_address', 'user')
    list_display_links = ('email', 'ip_address')

@admin.register(Comment)
class CommentAdminPage(DraggableMPTTAdmin):

    list_display = ('tree_actions', 'indented_title', 'women', 'author', 'time_create', 'status')
    mptt_level_indent = 2
    list_display_links = ('women',)
    list_filter = ('time_create', 'time_update', 'author')
    list_editable = ('status',)

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content', 'photo', 'slug', 'cat', 'husband', 'tags']
    #exclude = ['tags', 'is_published']
    readonly_fields = ['slug']
    filter_horizontal = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat', 'brief_info',)
    list_display_links = ('title', )
    ordering = ['time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов.'

    @admin.display(description='Фото', ordering='photo')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50")
        else:
            return 'Без фото'

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

#admin.site.register(Women, WomenAdmin)
