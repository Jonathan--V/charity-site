from django import forms

from django.forms import ModelForm

from main.models.main.person import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }
