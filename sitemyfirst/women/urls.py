from django.urls import path, register_converter
from . import views
from . import converters
from .views import CommentCreateView, FeedbackCreateView, RatingCreateView

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('post/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('rating/', RatingCreateView.as_view(), name='rating'),
]

#   re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
