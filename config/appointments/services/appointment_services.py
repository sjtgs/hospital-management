from django.core.exceptions import ValidationError
from appointments.models import Appointment

# Appointment Function to Schedule the Appointment
def schedule_appointment(patient, doctor,
                         appointment_date,
                         appointment_time,
                         reason=""):

    # Check doctor availability
    exists = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_date,
        appointment_time=appointment_time
    ).exists()

    if exists:
        raise ValidationError(
            "Doctor is already booked for this time slot"
        )

    appointment = Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        reason=reason
    )

    return appointment