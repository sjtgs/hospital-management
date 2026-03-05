from datetime import datetime
from django.core.exceptions import ValidationError

from appointments.models import Appointment
from appointments.services.scheduling_engine import (
    validate_doctor_schedule
)


def schedule_appointment(
    patient,
    doctor,
    appointment_date,
    appointment_time,
    reason=""
):
    """
    Creates a new appointment after validating scheduling rules.
    """

    appointment_datetime = datetime.combine(
        appointment_date,
        appointment_time
    )

    #  Future Date Validation 
    if appointment_datetime <= datetime.now():
        raise ValidationError(
            "Appointments must be scheduled for a future date and time."
        )

    # Doctor Availability Validation 
    validate_doctor_schedule(
        doctor,
        appointment_date,
        appointment_time
    )

    #  Create Appointment 
    appointment = Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        reason=reason
    )

    return appointment