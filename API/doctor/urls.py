from django.urls import path
from .views import DoctorCreateView

urlpatterns = [
    path('register/', DoctorCreateView.as_view(), name='doctor-register'),
]