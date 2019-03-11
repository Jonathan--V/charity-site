from django.forms import ModelForm

from main.models.main.contact_request import ContactRequest


class ContactForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = '__all__'
        localized_fields = '__all__'
