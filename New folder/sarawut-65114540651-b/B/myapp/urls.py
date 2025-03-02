from django.urls import path
from .views import showinfo
urlpatterns = [
    path("" ,showinfo.as_view(), name="filter")
]