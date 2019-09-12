from django.db import models

class PatientForm(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateTimeField(auto_now_add=False)
    collection = models.DateTimeField(auto_now_add=True)
    delivery = models.DateTimeField(auto_now_add=False)
    doctor = models.CharField(max_length=255)
    formId = models.CharField(max_length=255)