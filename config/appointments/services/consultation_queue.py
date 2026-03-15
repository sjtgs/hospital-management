from datetime import date
from appointments.models import Appointment

# Created function Queue of Patient Appointments 
def get_doctor_daily_queue(doctor):
    """
    Returns today's appointments for a doctor ordered by time.
    """

    today = date.today()

    appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=today,
        status__in=["vitals_recorded", "in_progress"]
    ).order_by("appointment_time")

    return appointments