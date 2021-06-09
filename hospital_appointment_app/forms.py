from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from .models import Appointment


#Appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'