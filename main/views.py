from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from main.forms.main.help_form import HelpForm
from main.forms.main.contact_form import ContactForm
from main.forms.main.person_form import PersonForm
from main.models.main.person import Person


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html', {})


class ContactRequestReceivedView(View):
    def get(self, request):
        return render(request, 'main/contact_request_received.html', {})


class HelpRequestReceivedView(View):
    def get(self, request):
        return render(request, 'main/help_request_received.html', {})


class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_request_received/')
        else:
            return render(request, 'main/contact.html', {'form': form})

    def get(self, request):
        return render(request, 'main/contact.html', {'form': ContactForm()})


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html', {})


class HelpRequestView(View):
    def post(self, request):
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person = person_form.save()
            request.session['HelpRequestView']['person_id'] = person.pk
            return HttpResponseRedirect('/help_request_page_2/')
        else:
            return render(request, 'main/help_request.html', {'form': person_form})

    def start(self, request):
        request.session['HelpRequestView'] = {}
        return render(request, 'main/help_request.html', {'form': PersonForm()})

    def get(self, request):
        return self.start(request)


class HelpRequestPage2View(View):
    def post(self, request):
        help_request_form = HelpForm(request.POST)
        if help_request_form.is_valid():
            person_id = request.session['HelpRequestView']['person_id']
            help_request = help_request_form.save(commit=False)
            help_request.person_id = person_id
            help_request_form.save()
            return HttpResponseRedirect('/help_request_received/')
        else:
            return render(request, 'main/help_request.html', {'form': help_request_form})

    def get(self, request):
        return render(request, 'main/help_request.html', {'form': HelpForm()})


# class HelpRequestView(View):
#     def post(self, request):
#         print(request.session['HelpRequestView']['current_form_name'])
#         if not request.session['HelpRequestView']:
#             return self.start(request)
#         if request.session['HelpRequestView']['current_form_name'] == 'person_form':
#             person_form = PersonForm(request.POST)
#             # check whether it's valid:
#             if person_form.is_valid():
#                 request.session['HelpRequestView']['person_form'] = person_form
#                 print("reached0")
#                 request.session['HelpRequestView']['current_form_name'] = 'help_request_form'
#                 print(request.session['HelpRequestView']['current_form_name'])
#                 return render(request, 'main/help_request.html', {'form': HelpForm})
#             else:
#                 return render(request, 'main/help_request.html', {'form': PersonForm})
#         elif request.session['HelpRequestView']['current_form_name'] == 'help_request_form':
#             print("reached0.5")
#             help_request_form = HelpForm(request.POST)
#             # check whether it's valid:
#             print("reached1")
#             if help_request_form.is_valid():
#                 print("reached2")
#
#                 person_form = request.session['HelpRequestView']['person_form']
#                 person_form.save()
#                 help_request_form.cleaned_data['person'] = person_form.cleaned_data['person']
#                 help_request_form.save()
#                 return HttpResponseRedirect('/help_request_received/')
#             else:
#                 return render(request, 'main/help_request.html', {'form': HelpForm})
#         else:
#             return self.start(request)
#
#     def start(self, request):
#         print("start called")
#         request.session['HelpRequestView'] = {}
#         request.session['HelpRequestView']['current_form_name'] = 'person_form'
#         return render(request, 'main/help_request.html', {'form': PersonForm()})
#
#     def get(self, request):
#         return self.start(request)


# class HelpRequestView(SessionWizardView):
#     form_list = [PersonForm, HelpForm]
#
#     def done(self, form_list, **kwargs):
#         person_form = kwargs['form_dict']['0']
#         person_form.save()
#         # help_form.cleaned_data['Person'] = PersonForm.cleaned_data['Person']
#
#         person_data = self.get_form_step_data(person_form)
#         person = person_data.get('person','')
#         self.initial_dict.get(2, {'person': person})
#         help_form = kwargs['form_dict']['1']
#         help_form.save()
#
#         return HttpResponseRedirect('/help_request_received/')
