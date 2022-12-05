from django.test import TestCase

from restaurant.forms import CookCreationForm, CookExperienceUpdateForm


class FormsTests(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "test_username",
            "password1": "test_password1234",
            "password2": "test_password1234",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 55,
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_update_form(self):
        form_data = {"years_of_experience": 5}

        form = CookExperienceUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
