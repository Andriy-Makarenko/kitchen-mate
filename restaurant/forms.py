from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Dish, Cook


class DishForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_license_number(self):  # this logic is optional, but possible
        return validate_experience(self.cleaned_data["years_of_experience"])


def validate_experience(
    years_of_experience,
):  # regex validation is also possible here
    if years_of_experience > 60:
        raise ValidationError("Experience can not be more than 60 years")
    if years_of_experience < 1:
        raise ValidationError("We need experience chef on the kitchen")

    return years_of_experience
