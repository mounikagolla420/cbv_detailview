from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.
from app.models import *


class home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'