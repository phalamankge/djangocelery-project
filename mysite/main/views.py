from django.shortcuts import render
#mysite/main/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test

# Create your views here.
def home(request):
  test.delay(15)
  return HttpResponse("Hey there!")
