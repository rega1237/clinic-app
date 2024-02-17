from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorCreateSerializer, DoctorSerializer, SpecializationSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Specialization

class DoctorCRUDView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = DoctorSerializer(Doctor.objects.get(user=request.user))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DoctorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        doctor = Doctor.objects.get(user=request.user)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        doctor = Doctor.objects.get(user=request.user)
        doctor.delete()
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SpecializationCRUDView(APIView):
    def get(self, request):
        serializer = SpecializationSerializer(Specialization.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
