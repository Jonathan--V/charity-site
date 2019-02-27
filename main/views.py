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
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_request_received/')
        else:
            return render(request, 'contact.html', {'form': form})

    def get(self, request):
        return render(request, 'contact.html', {'form': ContactForm()})


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})
