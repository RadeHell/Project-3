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

def Orders(request):
  if request.method =="POST":
    form = Order(render.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      greeting = f"Hi, {first_name} {last_name}!"
      print("greetins")
      return render(request, 'home.html')
  else:
    form = OrderForm()