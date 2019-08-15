from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor/', views.editor, name="editor"),
    path('home/', views.home, name="home"),
    path('conc/', views.conc, name="conc"),
    path('conc2/', views.conc2, name="conc2"),
]
