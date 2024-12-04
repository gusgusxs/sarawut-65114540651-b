from django.shortcuts import render
from django.views.generic import ListView
from .models import coruse
# Create your views here.

class showinfo(ListView):
    model = coruse
    context_object_name = coruse
    template_name = ('show.html')
    fileds = ['id','name','info']