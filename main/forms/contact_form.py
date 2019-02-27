from django.forms import ModelForm

from main.models.main.contact_request_model import ContactRequestModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactRequestModel
        fields = '__all__'
