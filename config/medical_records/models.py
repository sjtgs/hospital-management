from django.db import models
from django.core.exceptions import ValidationError
from appointments.models import Appointment

# Create class for Medical Records 
class MedicalRecord(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="medical_record"
    )

    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """
        Ensure vitals exist before a medical record is created.
        """
        if not self.appointment.vitals.exists():
            raise ValidationError(
                "Vitals must be recorded before creating a medical record"
            )


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Medical Record for {self.appointment.patient}"


# Class to record Vitals for the Patient
class Vitals(models.Model):

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="vitals"
    )

    temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        help_text="Body temperature in Celsius"
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Weight in kilograms"
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Height in centimeters"
    )

    heart_rate = models.PositiveIntegerField(
        help_text="Beats per minute"
    )

    blood_pressure = models.CharField(
        max_length=15,
        help_text="Example: 120/80"
    )

    recorded_by = models.CharField(
        max_length=100,
        help_text="Name of the nurse recording vitals"
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Vitals for {self.appointment.patient}"