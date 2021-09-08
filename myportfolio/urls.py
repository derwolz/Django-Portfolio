from django.urls import path
from . import views

urlpatterns = [
    #leave as empty string
    path("", views.index, name="index"),
    path('projects/',views.projects, name='projects'),
    path(r'contact/', views.contact, name='contact'),
    
    ]
