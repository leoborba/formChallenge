from django.shortcuts import get_object_or_404

from medicalRecord.models import PatientForm


def add_patient(name,birth,collection,doctor,form_id):
    try:
        patient = PatientForm()
        result = update_patient(patient,name,birth,collection,None,doctor,form_id)

        if result:
            return True
        else:
            return False
    except:
        return False


def update_patient(patient_instance,name,birth,collection,delivery,doctor,form_id):
    try:
        if patient_instance:
            patient_instance.name = name
            patient_instance.birth = birth
            patient_instance.collection = collection

            if delivery is not None and delivery != '' :
                patient_instance.delivery = delivery

            patient_instance.doctor = doctor
            patient_instance.formId = form_id

            patient_instance.save()
            return True
        else:
            return False
    except Exception as e:
        s = str(e)
        return False