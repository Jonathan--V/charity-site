from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    area_of_responsibility = models.CharField(_('Area of responsibility'), max_length=200)
    title = models.CharField(_('Title'), max_length=20)
    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('Last name'), max_length=100)
    email_address = models.EmailField(_('Email address'))
    publicly_viewable = models.BooleanField(_('Publicly viewable'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['id']
