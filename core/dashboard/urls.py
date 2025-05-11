from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('general/', views.general_dashboard, name='general_dashboard'),
    path('default/', views.default_dashboard, name='default_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('take-appointment/<int:doctor_id>/', views.take_appointment, name='take_appointment'),
    path('delete-appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),

]
