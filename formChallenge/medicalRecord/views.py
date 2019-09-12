from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from medicalRecord.forms import PatientFormPOST
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