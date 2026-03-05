from django.db import models

# Create Doctor Model 


class Doctor(models.Model):

    name = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name