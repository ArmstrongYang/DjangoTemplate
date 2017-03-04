"""
Definition of models.
"""
import os
from django.db import models
import scipy.io as sio
import json
from Infinity.settings import STATICFILES_DIRS as DIRS
from highcharts import Highchart    #该模块直接生成网页.html

def search_in_base_dir(filename):
    for file in DIRS:
        path = file + filename
        if os.path.exists(path):
            return path
    raise Exception

def load_alldata(length):
    if length<=0:
        raise ValueError

    content = sio.loadmat('E:/Documents/VerityCloud/MIMIC2DB/a44091cm/a44091cm.mat')
    if length>len(x[0]):
        raise OverflowError
    x = content['val'].tolist()
    y = x[0][0:length]
    #print(y)
    z = [[0 for col in range(2)] for row in range(length)]
    for i in range(length):
        z[i][0] = i/125
        z[i][1] = y[i]
    
    #lst = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 40]
    lst = z
    return json.dumps(lst)

def load_data():
    content = sio.loadmat('E:/Documents/VerityCloud/MIMIC2DB/a44091cm/a44091cm.mat')
    x = content['val'].tolist()
    y = x[0][0:1000]
    #print(y)
    z = [[0 for col in range(2)] for row in range(1000)]
    for i in range(1000):
        z[i][0] = i/125
        z[i][1] = y[i]
    
    #lst = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 40]
    lst = z
    return json.dumps(lst)

def pressure2altitude(p):
    p0 = 1013.25    #sea level pressure, uint:hPa
    return int(44330 * (1-(p/p0)**(1/5.255)))

def altitude_pressure():
    p_start = 300
    p_end = 1100
    p_step = 0.1
    p_len = p_end-p_start
    p_num = int(p_len/p_step+1)
    series = [[0 for col in range(2)] for row in range(p_num)]
    for i in range(p_num):
        series[i][0] = p_start+i*p_step
        series[i][1] = pressure2altitude(series[i][0])
    
    return json.dumps(series)


def load_data_filename(filename):
    path = search_in_base_dir(filename)
    content = sio.loadmat(path)
    index_begin = 1600
    index_end = 2600
    x = content['ppg_data'].tolist()
    y = x[0][index_begin:index_end]
    #print(y)
    z = [[0 for col in range(2)] for row in range(1000)]
    for i in range(1000):
        z[i][0] = i/100
        z[i][1] = y[i]
    
    #lst = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 40]
    lst = z
    return json.dumps(lst)

def hchart_json():
    chart = Highchart()
    data = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    chart.add_data_set(data, series_type='line', name='Example Series')
    chart.save_file()

def hchart_str():
    hchart_json()
    strx = r'''{
            title: {
                text: 'Test',
                //x: -20 //center
            },
            xAxis: {
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            },
            yAxis: {
                title: {
                    text: 'Temperature (°C)'
                },
            },
            series: [{
                name: 'London',
                data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            }]
        }'''
    return strx

if __name__ == '__main__':
    path = search_in_base_dir('verity/ppg_RawDataSheet1.mat')
    print(path)