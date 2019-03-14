from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    name = models.CharField(_('name'), max_length=50)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(_('location'), max_length=50)
    date = models.DateField(_('date'))
    description = models.TextField(_('description'), max_length=1000)

    def __str__(self):
        return f'{str(self.name)} - {str(self.date)}'
