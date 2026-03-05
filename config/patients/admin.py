from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "patient_id",
        "first_name",
        "last_name",
        "guardian",
        "date_registered"
    )

    search_fields = (
        "patient_id",
        "first_name",
        "last_name",
    )

    list_filter = ("date_registered",)