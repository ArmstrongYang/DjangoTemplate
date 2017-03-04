from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from . import models

# Create your views here.

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'family/index.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
        }
    )

def device(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'family/device.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
        }
    )


def contact(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'family/contact.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
        }
    )

def about(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'family/about.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
        }
    )
