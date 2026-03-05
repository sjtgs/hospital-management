from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

from appointments.models import Appointment


APPOINTMENT_DURATION = timedelta(minutes=45)


def validate_doctor_schedule(doctor, appointment_date, appointment_time):
    """
    Validates whether a doctor is available for a given appointment slot.

    Checks:
    1. Appointment is within doctor's working hours
    2. Appointment does not overlap with existing bookings
    """

    appointment_datetime = datetime.combine(
        appointment_date,
        appointment_time
    )

    # --- Check working hours ---
    if not (
        doctor.work_start_time
        <= appointment_time
        <= doctor.work_end_time
    ):
        raise ValidationError(
            "Appointment is outside doctor's working hours."
        )

    # --- Get existing appointments for that doctor on that date ---
    existing_appointments = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_date
    )

    for appointment in existing_appointments:

        existing_start = datetime.combine(
            appointment.appointment_date,
            appointment.appointment_time
        )

        existing_end = existing_start + APPOINTMENT_DURATION

        new_end = appointment_datetime + APPOINTMENT_DURATION

        #  Overlap Detection 
        if appointment_datetime < existing_end and new_end > existing_start:
            raise ValidationError(
                "Doctor already has an appointment in this time slot."
            )