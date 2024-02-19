from rest_framework import serializers
from .models import Doctor, Specialization
from authentication.models import User

# User serializer to be used in DoctorSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class SpecializationSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = Specialization
        fields = ["id", "name", "doctor_name"]

    def get_doctor_name(self, obj):
        doctors = obj.doctors.all()
        return [
            doctor.user.first_name + " " + doctor.user.last_name for doctor in doctors
        ]


class DoctorCreateSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ["phone_number", "medical_college_reg_number", "specializations"]


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    specializations = SpecializationSerializer(many=True)

    class Meta:
        model = Doctor
        fields = [
            "user",
            "phone_number",
            "medical_college_reg_number",
            "specializations",
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user
        user.email = user_data.get("email", user.email)
        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.save()
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.medical_college_reg_number = validated_data.get(
            "medical_college_reg_number", instance.medical_college_reg_number
        )
        instance.save()
        return instance


class DoctorShowSerializer(serializers.ModelSerializer):
    specializations = SpecializationSerializer(many=True, read_only=True)

    user_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = [
            "user_full_name",
            "phone_number",
            "medical_college_reg_number",
            "specializations",
        ]

    def get_user_full_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name
