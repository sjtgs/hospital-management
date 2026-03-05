from patients.models import Patient

# Create a Patient function  
def create_patient(guardian, first_name, last_name,
                   date_of_birth, gender,
                   blood_group="", allergies="", notes=""):

    patient = Patient(
        guardian=guardian,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender,
        blood_group=blood_group,
        allergies=allergies,
        notes=notes
    )

    patient.save()
    return patient