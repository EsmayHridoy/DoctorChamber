from django.shortcuts import render, redirect
from registration.models import User
from datetime import date
from django.utils.crypto import get_random_string
from .models import Appointment
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

@csrf_exempt
def doctor_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    doctor = User.objects.get(id=user_id)

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        is_completed = request.POST.get('is_completed') == 'on'
        comment = request.POST.get('comment')

        appointment = Appointment.objects.get(id=appointment_id)
        appointment.is_completed = is_completed
        appointment.comment = comment
        appointment.save()

    appointments = Appointment.objects.filter(doctor=doctor).order_by('appointment_date', 'serial_number')

    return render(request, 'dashboard/doctor_dashboard.html', {
        'appointments': appointments
    })

def general_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)
    if user.role.role.lower() != 'general':
        return redirect('login')  # or show error

    doctors = User.objects.filter(role__role__iexact='Doctor')
    appointments = Appointment.objects.filter(patient=user).order_by('-appointment_date')

    return render(request, 'dashboard/general_dashboard.html', {
        'doctors': doctors,
        'appointments': appointments
    })

def default_dashboard(request):
    return render(request, 'dashboard/default_dashboard.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def take_appointment(request, doctor_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    patient = User.objects.get(id=user_id)
    doctor = User.objects.get(id=doctor_id)
    today = date.today()
    serial = Appointment.objects.filter(doctor=doctor, appointment_date=today).count() + 1
    token = f"{doctor_id}{user_id}{get_random_string(5).upper()}"
    appointment = Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        appointment_date=today,
        serial_number=serial,
        token_number=token
    )

    return render(request, 'dashboard/appointment_confirmed.html', {
        'appointment': appointment
    })

@csrf_exempt
def delete_appointment(request, appointment_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        appointment = Appointment.objects.get(id=appointment_id, patient_id=user_id)
        appointment.delete()
    except Appointment.DoesNotExist:
        pass

    return redirect('general_dashboard')



