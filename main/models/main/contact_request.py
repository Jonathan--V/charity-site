from django.db import models


class ContactRequest(models.Model):
    subject = models.CharField(max_length=200)
    email_address = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=20000)

    def __str__(self):
        return self.subject
