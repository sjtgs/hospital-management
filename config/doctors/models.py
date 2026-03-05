from django.db import models

# Create Doctor Model 
class Doctor(models.Model):

    name = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    working_start_time = models.TimeField(default="08:00")
    working_end_time = models.TimeField(default="17:00")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name