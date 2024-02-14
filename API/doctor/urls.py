from django.urls import path
from .views import DoctorCRUDView

urlpatterns = [
    path('profile/', DoctorCRUDView.as_view(), name='doctor-profile'),
]