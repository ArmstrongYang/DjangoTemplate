from django.shortcuts import render
from datetime import datetime
from . import models

# Create your views here.

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/index.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
        }
    )

