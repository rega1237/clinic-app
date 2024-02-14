from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = ["phone_number", "medical_college_reg_number"]