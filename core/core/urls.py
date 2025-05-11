# core/urls.py
from django.contrib import admin
from django.urls import path, include  # Import include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='home'), 
    path('registration/', include('registration.urls')),
    path('login/', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
]