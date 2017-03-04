"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from . import models
import json
from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'research/index.html',
        {
            'title':'Health Infinity',
            'info' :'Medical BigData Platform',
            'year' : datetime.now().year,
            'temp': models.load_data(),
            'test': models.hchart_str(),
        }
    )

def chart(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    filename = 'ppg_RawDataSheet13.mat'
    subtitle = 'VerityDB/' + filename
    return render(
        request,
        'research/chart.html',
        {
            'title':'Chart',
            'message':'Highcharts Based',
            'year':datetime.now().year,
            #'data': content['val'][0:11]
            'temp': models.load_data(),
            'test': models.load_data_filename(filename),
            'subtitle_text': subtitle,
        }
    )
def barometric(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    filename = 'ppg_RawDataSheet13.mat'
    #subtitle = 'VerityDB/' + filename
    subtitle = '基于海拔和气压的通用公式'
    return render(
        request,
        'research/barometric.html',
        {
            'title':'Chart',
            'message':'Highcharts Based',
            'year':datetime.now().year,
            'data': models.altitude_pressure(),
            'subtitle_text': subtitle,
        }
    )
class BarView(HighChartsMultiAxesView):
    title = 'Test Bar Chart @17:15'
    subtitle = 'my subtitle'
    categories = ['Orange', 'Bananas', 'Apples']
    chart_type = ''
    chart = {'zoomType': 'xy'}
    tooltip = {'shared': 'true'}
    legend = {'layout': 'horizontal', 'align': 'left',
              'floating': 'true', 'verticalAlign': 'top',
              'y': -10, 'borderColor': '#e3e3e3'}

    @property
    def yaxis(self):
        y_axis = [
            {'labels': {'format': '{value} pz/sc ', 'style': {'color': '#f67d0a'}},
             'title': {'text': "Oranges", 'style': {'color': '#f67d0a'}},
             'opposite': 'true'},
            {'gridLineWidth': 1,
             'title': {'text': "Bananas", 'style': {'color': '#3771c8'}},
             'labels': {'style': {'color': '#3771c8'}, 'format': '{value} euro'}},
            {'gridLineWidth': 1,
             'title': {'text': "Apples", 'style': {'color': '#666666'}},
             'labels': {'format': '{value} pz', 'style': {'color': '#666666'}},
             'opposite': 'true'}
        ]
        return y_axis

    @property
    def series(self):
        series = [
            {
                'name': 'Orange',
                'type': 'column',
                'yAxis': 1,
                'data': [90,44,55,67,4,5,6,3,2,45,2,3,2,45,5],
                'tooltip': "{ valueSuffix: ' euro' }",
                'color': '#3771c8'
            },
            {
                'name': 'Bananas',
                'type': 'spline',
                'yAxis': 2,
                'data': [12,34,34,34, 5,34,3,45,2,3,2,4,4,1,23],
                'marker': { 'enabled': 'true' },
                'dashStyle': 'shortdot',
                'color': '#666666',
                },
            {
                'name': 'Apples',
                'type': 'spline',
                'data': [12,23,23,23,21,4,4,76,3,66,6,4,5,2,3],
                'color': '#f67d0a'
            }
        ]
        return series

def hchart_para(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    try: 
        a = request.GET['a']
        BarView.title='Hello from parameter' + str(a)
    except:
        a = 0
    return render(
        request,
        'research/bar.html',
        {
            'title':'Chart',
            'message':'Highcharts Based',
            'year':datetime.now().year,
            'hchart_url':'bar',
            'hchart_para': a,
        }
    )


def hchart(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'research/bar.html',
        {
            'title':'Chart',
            'message':'Highcharts Based',
            'year':datetime.now().year,
            'hchart_url':'bar',
        }
    )
