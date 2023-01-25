from django import forms
from . models import PatientModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PatientForm(forms.ModelForm):
   class Meta:
       model = PatientModel
       fields = '__all__'

class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


