from django import forms

from medicalRecord.models import PatientForm


class PatientFormPOST(forms.ModelForm):
    class Meta:
        model = PatientForm
        fields = ('name', 'doctor',)