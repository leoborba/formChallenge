from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from medicalRecord.models import PatientForm


def medicalRecord_index(request):
    if request.method == 'POST':
        patient = PatientForm(
            name = request.POST.get('name'),
            birth = request.POST.get('birth'),
            collection = request.POST.get('collection'),
            delivery = request.POST.get('delivery'),
            doctor = request.POST.get('doctor'),
            formId = request.POST.get('formid')
        )
        patient.save()
        return HttpResponseRedirect(request.path_info)

    forms = PatientForm.objects.all().order_by('-collection')
    context = {
        "forms": forms,
    }
    return render(request, "medicalRecord_index.html", context)


def medicalRecord_detail(request, pk):
    patient = PatientForm.objects.get(pk=pk)

    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        #if form.is_valid():
        #    doctor = Doctor(
        #        name=form.cleaned_data["name"],
        #        doctorId=form.cleaned_data["doctorId"],
        #        patientForm=patientForm
        #    )
        #    doctor.save()

    #comments = Doctor.objects.filter(patientForm=patientForm)
    context = {
        "patient": patient,
        #"doctor": doctor,
        "form": form,
    }
    return render(request, "medicalRecord_detail.html", context)


def updatePatient(request, pk):
    patient_instance = get_object_or_404(PatientForm, pk=pk)

    if request.method == 'POST':
        patient_instance.name = request.POST.get('name')
        patient_instance.birth = request.POST.get('birth')
        patient_instance.collection = request.POST.get('collection')
        delivery = request.POST.get('delivery')

        if delivery != '':
            patient_instance.delivery = delivery

        patient_instance.doctor = request.POST.get('doctor')
        patient_instance.formId = request.POST.get('formid')

        patient_instance.save()

    forms = PatientForm.objects.all().order_by('-collection')
    context = {
        "forms": forms,
    }
    return render(request, "medicalRecord_index.html", context)