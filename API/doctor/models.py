from django.db import models
from authentication.models import User
# Create your models here.

class Doctor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=15)
  medical_college_reg_number = models.CharField(max_length=20)

  def __str__(self):
    return f"Dr. {self.user.first_name} {self.user.last_name} - {self.medical_college_reg_number}"
  
class Specialization(models.Model):
  name = models.CharField(max_length=100)
  doctors = models.ManyToManyField(Doctor, related_name='specializations', blank=True)

  def __str__(self):
    return self.name
