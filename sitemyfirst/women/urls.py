from django.urls import path, register_converter, include
from rest_framework import routers

from . import views
from . import converters
from .views import CommentCreateView, FeedbackCreateView, RatingCreateView, WomenViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

register_converter(converters.FourDigitYearConverter, 'year4')

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet, basename='women')

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
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
