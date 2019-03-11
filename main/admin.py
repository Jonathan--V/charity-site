from django.contrib import admin

from main.models.main.contact import Contact
from main.models.main.contact_request import ContactRequest
from main.models.main.help_request import HelpRequest
from main.models.main.person import Person

admin.site.register(ContactRequest)
admin.site.register(HelpRequest)
admin.site.register(Person)
admin.site.register(Contact)
