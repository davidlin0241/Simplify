from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
  
def editor(request):
  return render(request, 'editor.html')

def home(request):
  return render(request, 'home.html')
