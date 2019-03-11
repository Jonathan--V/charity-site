from django import forms

from django.forms import ModelForm

from main.models.main.person import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        localized_fields = '__all__'
        widgets = {
            'date_of_birth': forms.widgets.DateInput(attrs={'type': 'date'})
        }
