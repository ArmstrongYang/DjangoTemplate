"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from main.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/index.html',
        {
            'title':'Infinity ',
            'message':'',
            'info' :'Web Resource Platform',
            'info-cn':'网络资源学习和管理平台',
            'year' : datetime.now().year,
        }
    )

def blog(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/blog.html',
        {
            'title':'Blog',
            'message':'Blog Management',
            'info' :'Web Resource Platform',
            'info-cn':'网络资源学习和管理平台',
            'year':datetime.now().year,
        }
    )

def family(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/family.html',
        {
            'title':'Family',
            'message':'Family Management',
            'info' :'Web Resource Platform',
            'info-cn':'网络资源学习和管理平台',
            'year':datetime.now().year,
        }
    )

def research(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/research.html',
        {
            'title':'Research',
            'message':'Research',
            'info' :'Web Resource Platform',
            'info-cn':'网络资源学习和管理平台',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/about.html',
        {
            'title':'About',
            'message':'About me',
            'info' :'Web Resource Platform',
            'info-cn':'网络资源学习和管理平台',
            'year':datetime.now().year,
        }
    )

