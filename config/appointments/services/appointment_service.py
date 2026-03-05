from datetime import datetime
from django.core.exceptions import ValidationError
from appointments.models import Appointment
from doctor.models import Doctor

# Appointment Function to Schedule the Appointment
def schedule_appointment(patient, doctor,
                         appointment_date,
                         appointment_time,
                         reason=""):

    #  Future Date Validation
    appointment_datetime = datetime.combine(
        appointment_date,
        appointment_time
    )

    if appointment_datetime <= datetime.now():
        raise ValidationError(
            "Appointments must be scheduled for future date and time"
        )

    # Doctor Availability Check
    exists = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_date,
        appointment_time=appointment_time
    ).exists()

    if exists:
        raise ValidationError(
            "Selected doctor is not available at this time"
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