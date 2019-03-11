from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    title = models.CharField(_('title'), max_length=20)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    email_address = models.EmailField(_('email address'))
    date_of_birth = models.DateField(_('date of birth'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
