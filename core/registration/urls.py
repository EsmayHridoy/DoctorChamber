# registration/urls
from django.urls import path, include  # Import include
from . import views


urlpatterns = [
    path('', views.registration, name='registration_form'), 
]