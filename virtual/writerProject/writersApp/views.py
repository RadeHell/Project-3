from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def Main(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def Writers(request):
  template = loader.get_template('Writers.html')
  return HttpResponse(template.render())

def Books(request):
  template = loader.get_template('BestBooks.html')
  return HttpResponse(template.render())