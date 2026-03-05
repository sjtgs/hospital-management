from visits.models import Visit


# Create Visit Fuction to record the Visit of Patient at the Hospital
def record_visit(patient, doctor, appointment,
                 symptoms, diagnosis,
                 treatment="", prescription=""):

    visit = Visit.objects.create(
        patient=patient,
        doctor=doctor,
        appointment=appointment,
        symptoms=symptoms,
        diagnosis=diagnosis,
        treatment=treatment,
        prescription=prescription
    )

    return visit