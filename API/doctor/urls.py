from django.urls import path
from .views import DoctorShow, DoctorCRUDView, AllSpecializations, SpecializationShowDelete, SpecializationCreate

urlpatterns = [
    path('<int:pk>/', DoctorShow.as_view(), name='doctor'), # Get doctor info by id
    path('profile/', DoctorCRUDView.as_view(), name='doctor-profile'), # Create, update and delete doctor profile
    path('specializations/all/', AllSpecializations.as_view(), name='specializations'), # Get all the specializations
    path('specialization/<int:pk>/', SpecializationShowDelete.as_view(), name='specialization'), # Get specific specialization
    path('specialization/create/', SpecializationCreate.as_view(), name='create-specialization') # Create new specialization
]