from django.shortcuts import render
from django.views.generic import ListView
from .models import Classroom

class ListIndexView(ListView):
    template_name = 'index.html'
    model = Classroom