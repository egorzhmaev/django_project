# Generated by Django 4.2.1 on 2024-04-04 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('m_count', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Публикация')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='women.category', verbose_name='Категории')),
                ('husband', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='women', to='women.husband')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='women.tagpost', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Известные женщины',
                'verbose_name_plural': 'Известные женщины',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('viewed_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')),
                ('women', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='women.women')),
            ],
            options={
                'verbose_name': 'Просмотр',
                'verbose_name_plural': 'Просмотры',
                'ordering': ('-viewed_on',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'Нравится'), (-1, 'Не нравится')], verbose_name='Значение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Адрес')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('women', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='women.women', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
                'ordering': ('-time_create',),
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP отправителя')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'db_table': 'app_feedback',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=3000, verbose_name='Текст комментария')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'Черновик')], default='published', max_length=10, verbose_name='Статус поста')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='women.comment', verbose_name='Родительский комментарий')),
                ('women', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='women.women', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'app_comments',
                'ordering': ['-time_create'],
            },
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['-time_create'], name='women_women_time_cr_9f33c2_idx'),
        ),
        migrations.AddIndex(
            model_name='viewcount',
            index=models.Index(fields=['-viewed_on'], name='women_viewc_viewed__6bc790_idx'),
        ),
        migrations.AddIndex(
            model_name='rating',
            index=models.Index(fields=['-time_create', 'value'], name='women_ratin_time_cr_56bf74_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('women', 'ip_address')},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-time_create', 'time_update', 'status', 'parent'], name='app_comment_time_cr_0c0ec5_idx'),
        ),
    ]
