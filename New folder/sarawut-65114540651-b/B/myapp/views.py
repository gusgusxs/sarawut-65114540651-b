from django.shortcuts import render
from django.views.generic import ListView
from .models import coruse
# Create your views here.

class showinfo(ListView):
    model = coruse
    context_object_name = coruse
    template_name = 'filter.html'
    fileds = ['coruseid','name','info']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("search",'')

        if query:
            queryset = queryset.filter(coruseid__icontains=query)
            return queryset