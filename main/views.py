import re

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import resolve, reverse
from django.utils import translation
from django.views import View
from django.views.generic import ListView

from main.forms.main.help_form import HelpForm
from main.forms.main.contact_form import ContactForm
from main.forms.main.person_form import PersonForm
from main.models.main.contact import Contact


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html', {})


class ContactRequestReceivedView(View):
    def get(self, request):
        return render(request, 'main/contact_request_received.html', {})


class RequestHelpReceivedView(View):
    def get(self, request):
        return render(request, 'main/request_help_received.html', {})


class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact_request_received_url_name'))
        else:
            return render(request, 'main/contact.html', {'form': form})

    def get(self, request):
        return render(request, 'main/contact.html', {'form': ContactForm()})


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html', {})


class RequestHelpView(View):
    def post(self, request):
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person = person_form.save()
            request.session['RequestHelpView']['person_id'] = person.pk
            return HttpResponseRedirect(reverse('request_help_page_2_url_name'))
        else:
            return render(request, 'main/request_help.html', {'form': person_form})

    def start(self, request):
        request.session['RequestHelpView'] = {}
        return render(request, 'main/request_help.html', {'form': PersonForm()})

    def get(self, request):
        return self.start(request)


class RequestHelpPage2View(View):
    def post(self, request):
        request_help_form = HelpForm(request.POST)
        if request_help_form.is_valid():
            person_id = request.session['RequestHelpView']['person_id']
            help_request = request_help_form.save(commit=False)
            help_request.person_id = person_id
            request_help_form.save()
            return HttpResponseRedirect(reverse('request_help_received_url_name'))
        else:
            return render(request, 'main/request_help.html', {'form': request_help_form})

    def get(self, request):
        return render(request, 'main/request_help.html', {'form': HelpForm()})


class DirectoryView(ListView):

    model = Contact
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SetLanguageView(View):
    def post(self, request):
        new_language = request.POST['language']
        previous = request.META['HTTP_REFERER']
        groups = re.fullmatch("(?:http://[^/]*)(/[a-zA-Z]{2}(?:-[a-zA-Z]{2})?/.*)", previous).groups()
        url_name = resolve(groups[0]).url_name
        translation.activate(new_language)
        target_url = reverse(url_name)
        return HttpResponseRedirect(target_url)
