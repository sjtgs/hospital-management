from django.db import models
from guardians.models import Guardian

# Create Patient Model
class Patient(models.Model):
    patient_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    guardian = models.ForeignKey(
        Guardian,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "Male"),
            ("female", "Female")
        ]
    )

    blood_group = models.CharField(
        max_length=5, blank=True
    )

    allergies = models.TextField(blank=True)

    notes = models.TextField(blank=True)

    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_id} - {self.first_name}"

    def save(self, *args, **kwargs):
        # Auto generate patient ID
        if not self.patient_id:
            last_patient = Patient.objects.order_by('-id').first()

            if last_patient and last_patient.patient_id:
                number = int(last_patient.patient_id.split('-')[1]) + 1
            else:
                number = 1

            self.patient_id = f"CH-{number:04d}"

        super().save(*args, **kwargs)
