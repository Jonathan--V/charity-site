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
from django.contrib import admin
from django.urls import path

from main.views import AboutView, ContactRequestReceivedView, ContactView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home_url_name'),
    path('about/', AboutView.as_view(), name = 'about_url_name'),
    path('contact/', ContactView.as_view(), name = 'contact_url_name'),
    path('contact_request_received/', ContactRequestReceivedView.as_view(), name = 'contact_request_received_url_name'),
]
