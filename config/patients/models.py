from django.db import models
from datetime import date 
from django.db import transaction
from guardians.models import Guardian

# Create Patient Model
class Patient(models.Model):
    patient_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False
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

    @property
    def age(self):
        today = date.today()

        years = today.year - self.date_of_birth.year
        months = today.month - self.date_of_birth.month

        if today.day < self.date_of_birth.day:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        return f"{years} years {months} months"

    def __str__(self):
        return f"{self.patient_id} - {self.first_name}"

    def save(self, *args, **kwargs):

        if not self.patient_id:

            with transaction.atomic():

                last_patient = (
                    Patient.objects
                    .select_for_update()
                    .order_by("id")
                    .last()
                )

                if last_patient and last_patient.patient_id:
                    last_id = int(last_patient.patient_id[1:])
                    new_id = last_id + 1
                else:
                    new_id = 1

                self.patient_id = f"P{new_id:05d}"

        super().save(*args, **kwargs)