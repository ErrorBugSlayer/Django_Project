from django.urls import path
from . import views  # Import views.py

urlpatterns = [
    path('', views.home, name='home'),  # Home page
]
