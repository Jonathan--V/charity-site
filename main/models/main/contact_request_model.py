from django.db import models


class ContactRequestModel(models.Model):
    email_address = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
