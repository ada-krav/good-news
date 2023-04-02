from django.test import TestCase
from agency.forms import RedactorCreationForm


class RedactorCreationFormTest(TestCase):
    def test_redactor_creation_form_valid(self):
        form_data = {
            "username": "redactor",
            "password1": "lkjhfdsa",
            "password2": "lkjhfdsa",
            "first_name": "",
            "last_name": "",
            "years_of_experience": 7,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_creation_form_not_valid(self):
        """test that years_of_experience is required"""
        form_data = {
            "username": "driver",
            "password1": "lkjhfdsa",
            "password2": "lkjhfdsa",
            "first_name": "",
            "last_name": "",
            "years_of_experience": "",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
