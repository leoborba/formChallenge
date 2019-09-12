from django.contrib import admin

# Register your models here.
from medicalRecord.models import PatientForm


class PatientFormAdmin(admin.ModelAdmin):
    pass

admin.site.register(PatientForm, PatientFormAdmin)