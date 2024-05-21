from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    nom = "folong emerson nouveaux"
    return HttpResponse(template.render({'var1':nom},request)) 
  
  
def news(request):
    template = loader.get_template('news.html')
    nom = "folong emerson nouveaux"
    return HttpResponse(template.render({'var1':nom},request)) 
  
  
  
def product(request):
    template = loader.get_template('product.html')
    nom = "folong emerson nouveaux"
    return HttpResponse(template.render({'var1':nom},request)) 
  
  
def contact(request):
    template = loader.get_template('contact.html')
    nom = "folong emerson nouveaux"
    return HttpResponse(template.render({'var1':nom},request)) 
  
  