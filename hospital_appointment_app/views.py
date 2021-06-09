from hospital_appointment_app.models import Appointment
from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib import messages

from .forms import AppointmentForm

# Create your views here.
def appointmnet(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            return redirect('appointment')

    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form' : form})
    