from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

def index(request):
    data = {
        'current_hour': int(datetime.now().strftime('%H')),
        'active_page': 'index'
    }
    return render(request, 'main/index.html', data)

def django_guide(request):
    return render(request, 'main/guide.html', {'active_page': 'django_guide'})

def parsing_tools(request):
    return render(request, 'main/tools.html', {'active_page': 'parsing_tools'})

def faq(request):
    return render(request, 'main/faq.html', {'active_page': 'faq'})