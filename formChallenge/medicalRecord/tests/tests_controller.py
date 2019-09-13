import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formChallenge.settings")
django.setup()

from unittest import TestCase
from medicalRecord.controllerPatient import update_patient, add_patient
from medicalRecord.models import PatientForm


class AuthorModelTest(TestCase):
    @classmethod
    def setUp(self):
        # Set up non-modified objects used by all test methods
        PatientForm.objects.create()

    def test_add_patient(self):
        result = add_patient('1', '2019-10-10', '2019-10-12', '1', '1')
        self.assertTrue(result)


    def test_add_patient_can_fail(self):
        result = add_patient('1', 'AA19-10-10', '2019-10-12', '1', '1')
        self.assertFalse(result)

        result = add_patient('1', '2019-10-10', 'AA19-10-11', '1', '1')
        self.assertFalse(result)


    def test_check_values_after_update(self):
        patient_form = PatientForm.objects.get(id=1)
        update_patient(patient_form, '1', '2019-10-10', '2019-10-11', '2019-10-12', '1', '1')
        self.assertEqual(patient_form.name,'1')
        self.assertEqual(patient_form.birth, '2019-10-10')
        self.assertEqual(patient_form.collection, '2019-10-11')
        self.assertEqual(patient_form.delivery, '2019-10-12')
        self.assertEqual(patient_form.doctor, '1')
        self.assertEqual(patient_form.formId, '1')


    def test_update_patient_form_can_ok(self):
        patient_form = PatientForm.objects.get(id=1)
        result = update_patient(patient_form,'1','2019-10-10','2019-10-10','2019-10-10','1','1')
        self.assertTrue(result)

    def test_update_patient_form_can_fail_invalid_date(self):
        patient_form = PatientForm.objects.get(id=1)
        result = update_patient(patient_form,'1','AA19-10-10','2019-10-10','2019-10-10','1','1')
        self.assertFalse(result)

        result = update_patient(patient_form, '1', '2019-10-10', 'AA19-10-10', '2019-10-10', '1', '1')
        self.assertFalse(result)

        result = update_patient(patient_form, '1', '2019-10-10', '2019-10-10', 'AA19-10-10', '1', '1')
        self.assertFalse(result)