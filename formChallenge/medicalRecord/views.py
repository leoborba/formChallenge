from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from medicalRecord.controllerPatient import add_patient, update_patient
from medicalRecord.models import PatientForm
from medicalRecord.serializers import PatientFormSerializer


def medicalRecord_index(request):
    forms = PatientForm.objects.all().order_by('-collection','name')
    context = {
        "forms": forms,
    }
    return render(request, "medicalRecord_index.html", context)


def medicalRecord_add(request):
    if request.method == 'POST':
        add_patient(request.POST.get('name'),
                    request.POST.get('birth'),
                    request.POST.get('collection'),
                    request.POST.get('doctor'),
                    request.POST.get('form_id')
                   )

    return HttpResponseRedirect('/medicalRecord/')


def medicalRecord_update(request, pk):
    if request.method == 'POST':
        patient_instance = get_object_or_404(PatientForm, pk=pk)
        update_patient(patient_instance,
                       request.POST.get('name'),
                       request.POST.get('birth'),
                       request.POST.get('collection'),
                       request.POST.get('delivery'),
                       request.POST.get('doctor'),
                       request.POST.get('form_id'),
                      )

    return HttpResponseRedirect('/medicalRecord/')


def medicalRecord_detail(request, pk):
    patient = PatientForm.objects.get(pk=pk)

    context = {
        "patient": patient,
    }

    return render(request, "medicalRecord_detail.html", context)


class PatientFormViewSet(generics.ListCreateAPIView):
    queryset = PatientForm.objects.all()
    serializer_class = PatientFormSerializer