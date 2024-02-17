from django.contrib import admin
from .models import Doctor, Specialization

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
  list_display = ['user', 'phone_number', 'medical_college_reg_number', 'get_specializations']

  def get_specializations(self, obj):
    return ", ".join([spec.name for spec in obj.specializations.all()])

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization)