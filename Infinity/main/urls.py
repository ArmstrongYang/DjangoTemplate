"""
Definition of urls for Django App.
"""

from django.conf.urls import url
import django.contrib.auth.views
from . import views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

site = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^family$', views.family, name='family'),
    url(r'^about', views.about, name='about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
