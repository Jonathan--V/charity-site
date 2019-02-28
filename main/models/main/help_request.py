from django.db import models

from main.models.main.person import Person


class HelpRequest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    brief_summary_of_difficulty = models.CharField(max_length=200)
    how_can_we_help_you = models.TextField(max_length=20000, verbose_name="How can we help you?")

    def __str__(self):
        return self.brief_summary_of_difficulty
