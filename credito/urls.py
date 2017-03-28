"""credito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from creditoapp.views import WerknemerCreateView, home, contact, WerknemerUpdate, werknemers_list, WerknemerDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^credito/werknemers', werknemers_list, name='werknemers_list'),
    url(r'^credito/create/$', WerknemerCreateView.as_view(), name='werknemer_create'),
    url(r'^credito/update/(?P<pk>\d+)$', WerknemerUpdate.as_view(), name='werknemer_update'),
    url(r'^credito/delete/(?P<pk>\d+)$', WerknemerDelete.as_view(), name='werknemer_delete'),
    url(r'^$', home, name='home'),
    url(r'^contact', contact, name='contact'),
]
