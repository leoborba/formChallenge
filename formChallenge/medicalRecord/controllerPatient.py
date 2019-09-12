from django.shortcuts import get_object_or_404

from medicalRecord.models import PatientForm


def add_patient(name,birth,collection,delivery,doctor,form_id):
    patient = PatientForm(
        name=name,
        birth=birth,
        collection=collection,
        delivery=delivery,
        doctor=doctor,
        formId=form_id
    )
    patient.save()


def update_patient(pk,name,birth,collection,delivery,doctor,form_id):
    patient_instance = get_object_or_404(PatientForm, pk=pk)

    if patient_instance:
        patient_instance.name = name
        patient_instance.birth = birth
        patient_instance.collection = collection
        delivery = delivery

        if delivery != '':
            patient_instance.delivery = delivery

        patient_instance.doctor = doctor
        patient_instance.formId = form_id

        patient_instance.save()