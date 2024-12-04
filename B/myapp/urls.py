from django.urls import path
from .views import * 
urlpatterns = [
    path('show',showinfo.as_view(),name="show")
]