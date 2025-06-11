from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .auth_views import CustomAuthToken,register_user


router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/auth/register/', register_user, name='api_register'),
]