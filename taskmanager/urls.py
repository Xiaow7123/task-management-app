"""
URL configuration for taskmanager project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # ← This line was missing!
    path('api-auth/', include('rest_framework.urls')),  # ← For DRF login
]