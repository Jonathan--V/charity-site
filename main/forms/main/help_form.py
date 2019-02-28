from django.forms import ModelForm

from main.models.main.help_request import HelpRequest


class HelpForm(ModelForm):
    class Meta:
        model = HelpRequest
        exclude = ['person']
