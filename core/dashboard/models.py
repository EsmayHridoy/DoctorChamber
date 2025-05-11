from django.db import models
from registration.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    serial_number = models.IntegerField()
    token_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment: {self.token_number} with Dr. {self.doctor.last_name}"