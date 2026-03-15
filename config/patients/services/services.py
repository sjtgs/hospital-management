from django.db.models import Q
from ..models import Patient


def search_patients(query):

    """
    Search patients using multiple fields.
    """

    if not query:
        return Patient.objects.none()

    patients = Patient.objects.select_related(
        "guardian"
    ).filter(
        Q(patient_id__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(guardian__first_name__icontains=query) |
        Q(guardian__last_name__icontains=query) |
        Q(guardian__phone_number__icontains=query)
    ).order_by("first_name")

    return patients