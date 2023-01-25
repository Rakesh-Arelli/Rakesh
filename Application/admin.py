from django.contrib import admin
from .models import PatientModel

# Register your models here.
@admin.register(PatientModel)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','Gender','startCity','Destination','price')