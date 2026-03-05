from django.contrib import admin
from .models import Guardian

@admin.register(Guardian)
class Guardiansdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "relationship")
    search_fields = ("first_name", "last_name", "phone_number")