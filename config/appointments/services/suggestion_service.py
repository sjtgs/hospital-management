from doctors.models import Doctor
from appointments.models import Appointment


# Create a suggestion Function for the Doctor see if the Doctor is available or not
def suggest_available_doctors(appointment_date, appointment_time):

    booked_doctors = Appointment.objects.filter(
        appointment_date=appointment_date,
        appointment_time=appointment_time
    ).values_list('doctor_id', flat=True)

    return Doctor.objects.filter(
        is_active=True
    ).exclude(
        id__in=booked_doctors
    )