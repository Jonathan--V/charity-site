from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactRequest(models.Model):
    subject = models.CharField(_('Subject'), max_length=200)
    email_address = models.EmailField(_('Email address'))
    name = models.CharField(_('Name'), max_length=100, blank=True)
    description = models.TextField(_('Description'), max_length=20000)

    def __str__(self):
        return self.subject
