from django.contrib import admin
from .models import MedicalRecord , Vitals

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = (
        "appointment",
        "notes",
        "created_at"
    )

    search_fields = (
        "appointment__patient__first_name",
        "appointment__patient__last_name"
    )

@admin.register(Vitals)
class VitalsAdmin(admin.ModelAdmin):
    list_display = ("appointment", "temperature", "weight","height","heart_rate",
    "blood_pressure", "recorded_by","recorded_at",
    )
    search_fields = (
        "appointment__patient__first_name",
        "appointment__patient__last_name",
    )