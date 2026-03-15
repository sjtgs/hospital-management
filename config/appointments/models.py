from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor


class AppointmentStatus(models.TextChoices):

    SCHEDULED = "scheduled", "Scheduled"
    CHECKED_IN = "checked_in", "Checked In"
    VITALS_RECORDED = "vitals_recorded", "Vitals Recorded"
    IN_CONSULTATION = "in_consultation", "In Consultation"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"
    NO_SHOW = "no_show", "No Show"

class Appointment(models.Model):

    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    reason = models.TextField(blank=True)

    status = models.CharField(
        max_length=30,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.SCHEDULED
    )

    checked_in_at = models.DateTimeField(null=True, blank=True)
    consultation_started_at = models.DateTimeField(null=True, blank=True)
    consultation_completed_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def check_in(self):

        if self.status != AppointmentStatus.SCHEDULED:
            raise ValueError(
                "Only scheduled appointments can be checked in"
            )

        self.status = AppointmentStatus.CHECKED_IN
        self.checked_in_at = timezone.now()
        self.save()


    def start_consultation(self):

        if self.status != AppointmentStatus.VITALS_RECORDED:
            raise ValueError(
                "Vitals must be recorded before consultation"
            )

        self.status = AppointmentStatus.IN_CONSULTATION
        self.consultation_started_at = timezone.now()
        self.save()

    def complete_consultation(self):

        if self.status != AppointmentStatus.IN_CONSULTATION:
            raise ValueError(
                "Consultation must start before completing"
            )

        self.status = AppointmentStatus.COMPLETED
        self.consultation_completed_at = timezone.now()
        self.save()

    def mark_no_show(self):

        if self.status != AppointmentStatus.SCHEDULED:
            raise ValidationError(
                "Only scheduled appointments can be marked as no-show"
            )

        appointment_datetime = datetime.combine(
            self.appointment_date,
            self.appointment_time
        )

        if appointment_datetime > timezone.now():
            raise ValidationError(
                "Cannot mark appointment as no-show before its scheduled time"
            )

        self.status = AppointmentStatus.NO_SHOW
        self.save()
        
    class Meta:
        unique_together = ['doctor', 'appointment_date', 'appointment_time']

    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"