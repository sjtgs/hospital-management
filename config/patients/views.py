from django.shortcuts import render
from .services.services import search_patients

# Create a Search Function for Patient
def patient_search(request):

    query = request.GET.get("q")

    patients = search_patients(query)

    context = {
        "query": query,
        "patients": patients
    }

    return render(
        request,
        "patients/search_results.html",
        context
    )