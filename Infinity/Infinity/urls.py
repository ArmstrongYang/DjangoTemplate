"""
Definition of urls for HealthInfinity.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.views.generic.base import RedirectView

import main.forms
import main.views

import blog.urls
import family.urls
import research.urls

#from main.urls import urlpatterns as ma_urls
#from research.urls import urlpatterns as da_urls
#from service.urls import urlpatterns as sv_urls


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', include(main.urls.site)),
    url(r'^$', main.views.home, name='main-home'),
    url(r'^blog$', main.views.blog, name='main-blog'),
    url(r'^family$', main.views.family, name='main-family'),
    url(r'^research$', main.views.research, name='main-research'),
    url(r'^about$', main.views.about, name='main-about'),

    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/image/HealthInfinite_32X32.ico')),
       
    url(r'^blog/', include(blog.urls.site)),
    url(r'^family/', include(family.urls.site)),
    url(r'^research/', include(research.urls.site)),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'main/login.html',
            'authentication_form': main.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
