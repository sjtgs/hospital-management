from django.utils import timezone
from ..models import Appointment, AppointmentStatus

def get_doctor_queue(doctor):
    """
    Returns the waiting queue for a specific doctor.
    Only patients who have checked in and had vitals recorded appear.
    """
    today = timezone.now().date()

    return Appointment.objects.filter(
        appointment_date=today,
        doctor=doctor,
        status__in=[
            AppointmentStatus.CHECKED_IN,
            AppointmentStatus.VITALS_RECORDED
        ]
    ).order_by("checked_in_at")