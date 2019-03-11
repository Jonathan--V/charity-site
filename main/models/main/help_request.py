from django.db import models

from main.models.main.person import Person
from django.utils.translation import ugettext_lazy as _


class HelpRequest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    brief_summary_of_difficulty = models.CharField(_("Brief summary of difficulty"), max_length=200)
    how_can_we_help_you = models.TextField(_("How can we help you?"), max_length=20000)

    def __str__(self):
        return self.brief_summary_of_difficulty
