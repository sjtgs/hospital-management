from appointments.models import Appointment


# Created Patient Medical History 
def get_patient_medical_history(patient):

    history = Appointment.objects.filter(
        patient=patient,
        status__in=["completed", "in_progress"]
    ).select_related(
        "doctor"
    ).prefetch_related(
        "vitals",
        "medical_record"
    ).order_by("-appointment_date", "-appointment_time")

    return history