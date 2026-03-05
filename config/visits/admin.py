from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class Visitadmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "appointment", "symptoms", "diagnosis","treatment","prescription","visit_date")
    search_fields = ("patient", "appointment",)