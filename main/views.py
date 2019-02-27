from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms.contact_form import ContactForm


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class ContactRequestReceivedView(View):
    def get(self, request):
        return render(request, 'contact_request_received.html', {})


class ContactView(View):
    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/contact_request_received/')
        else:
            return render(request, 'contact.html', {'form': form})

    def get(self, request):
        return render(request, 'contact.html', {'form': ContactForm()})


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})
