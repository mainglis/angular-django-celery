
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
#from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the report index.")