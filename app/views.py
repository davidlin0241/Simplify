from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
  
def editor(request):
  return render(request, 'editor.html')

def home(request):
  return render(request, 'home.html')

def conc(request):
  return render(request, 'conc.html')

def conc2(request):
  return render(request, 'conc2.html')

def child(request):
  return render(request, 'edit/child.html')

def general(request):
  return render(request, 'edit/general.html')

def teen(request):
  return render(request, 'edit/teen.html')