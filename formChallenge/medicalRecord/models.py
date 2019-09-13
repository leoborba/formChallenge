from django.db import models

class PatientForm(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateField(auto_now_add=False)
    collection = models.DateField(auto_now_add=False)
    delivery = models.DateField(auto_now_add=False)
    doctor = models.CharField(max_length=255)
    formId = models.CharField(max_length=255)