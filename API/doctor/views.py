from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorCreateSerializer, DoctorSerializer, DoctorShowSerializer, SpecializationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Doctor, Specialization

# Create, update and delete doctor profile

class DoctorCRUDView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        doctor = Doctor.objects.get(user=request.user)
        serializer = DoctorSerializer(doctor)
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

# Get doctor info by id

class DoctorShow(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorShowSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Get all the specializations

class AllSpecializations(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        serializer = SpecializationSerializer(Specialization.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class SpecializationShowDelete(APIView):
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        return super(SpecializationShowDelete, self).get_permissions()

    # Get specific specialization info
    
    def get(self, request, pk):
        specialization = Specialization.objects.get(pk=pk)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete specific specialization

    def delete(self, request, pk):
        specialization = Specialization.objects.get(pk=pk)
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create new specialization
class SpecializationCreate(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
