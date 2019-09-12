from django.urls import include
from django.urls import path
from medicalRecord import views

urlpatterns = [
    path("", views.medicalRecord_index, name="medicalRecord_index"),
    path("add_patient/", views.medicalRecord_add, name="medicalRecord_add"),
    path("<int:pk>/", views.medicalRecord_detail, name="medicalRecord_detail"),
    path("update_patient/<int:pk>/", views.medicalRecord_update, name="medicalRecord_update"),
    path("api-patients/", views.PatientFormViewSet.as_view(),name="apiPatients")
]