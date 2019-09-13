import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formChallenge.settings")
django.setup()

from unittest import TestCase
from medicalRecord.models import PatientForm


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        PatientForm.objects.create()

    def test_labels(self):
        author = PatientForm.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        field_label = author._meta.get_field('birth').verbose_name
        self.assertEquals(field_label, 'birth')
        field_label = author._meta.get_field('collection').verbose_name
        self.assertEquals(field_label, 'collection')
        field_label = author._meta.get_field('delivery').verbose_name
        self.assertEquals(field_label, 'delivery')
        field_label = author._meta.get_field('doctor').verbose_name
        self.assertEquals(field_label, 'doctor')
        field_label = author._meta.get_field('formId').verbose_name
        self.assertEquals(field_label, 'formId')


    def test_labels_max_length(self):
        author = PatientForm.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
        max_length = author._meta.get_field('doctor').max_length
        self.assertEquals(max_length, 255)
        max_length = author._meta.get_field('formId').max_length
        self.assertEquals(max_length, 255)




