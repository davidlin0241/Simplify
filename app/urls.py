from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor/', views.editor, name="editor"),
    path('home/', views.home, name="home"),
    path('conc/', views.conc, name="conc"),
    path('conc2/', views.conc2, name="conc2"),
    path('edit/child/', views.child, name="cEditor"),
    path('edit/general/', views.general, name="gEditor"),
    path('edit/teen/', views.teen, name="tEditor"),
    path('index2/', views.index2, name="index2"),
]
