from django.db import models


class Person(models.Model):
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return str(self.first_name) + str(self.last_name)
