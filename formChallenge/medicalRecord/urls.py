from django.urls import include
from django.urls import path
from medicalRecord import views

urlpatterns = [
    path("", views.medicalRecord_index, name="medicalRecord_index"),
    path("<int:pk>/", views.medicalRecord_detail, name="medicalRecord_detail"),
    path("updatePatient/<int:pk>/", views.updatePatient, name="updatePatient"),
    path("api-patients/", views.PatientFormViewSet.as_view(),name="apiPatients")
]