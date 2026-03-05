from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


# Create Visiting Model 
class Visit(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField(blank=True)
    prescription = models.TextField(blank=True)

    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit {self.id}"