"""CharitySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from main.views import AboutView, ContactRequestReceivedView, ContactView, HomeView, HelpRequestView, \
    HelpRequestReceivedView, HelpRequestPage2View, DirectoryView, SetLanguageView

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', HomeView.as_view(), name='home_url_name'),
    path(_('about/'), AboutView.as_view(), name='about_url_name'),
    path(_('contact/'), ContactView.as_view(), name='contact_url_name'),
    path(_('contact_request_received/'), ContactRequestReceivedView.as_view(),
         name='contact_request_received_url_name'),
    path(_('help_request/'), HelpRequestView.as_view(), name='help_request_url_name'),
    path(_('help_request_page_2/'), HelpRequestPage2View.as_view(), name='help_request_page_2_url_name'),
    path(_('help_request_received/'), HelpRequestReceivedView.as_view(), name='help_request_received_url_name'),
    path(_('directory/'), DirectoryView.as_view(), name='directory_url_name'),
    path(_('set_language/'), SetLanguageView.as_view(), name='set_language_url_name'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(_('events/'), include('events.urls')),
)
