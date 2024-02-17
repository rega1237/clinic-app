from rest_framework import serializers
from .models import Doctor, Specialization
from authentication.models import User

class SpecializationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Specialization
    fields = "__all__"

class DoctorCreateSerializer(serializers.ModelSerializer):
  specialization = SpecializationSerializer(many=True)

  class Meta:
    model = Doctor
    fields = ["phone_number", "medical_college_reg_number", "specializations"]

# User serializer to be used in DoctorSerializer

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["email", "first_name", "last_name"]

class DoctorSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  
  class Meta:
    model = Doctor
    fields = ["user", "phone_number", "medical_college_reg_number"]

  def update(self, instance, validated_data):
    user_data = validated_data.pop('user')
    user = instance.user
    user.email = user_data.get('email', user.email)
    user.first_name = user_data.get('first_name', user.first_name)
    user.last_name = user_data.get('last_name', user.last_name)
    user.save()
    instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    instance.medical_college_reg_number = validated_data.get('medical_college_reg_number', instance.medical_college_reg_number)
    instance.save()
    return instance