from hospital_appointment_app.models import Appointment
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import AppointmentForm, NewUserForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            return redirect('appointment')

    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form' : form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = NewUserForm()
    return render(request=request, template_name ='register.html', context={'form':form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('appointment')
            #else:
                #pass
    else:
        form = AuthenticationForm(request.POST)
    return render(request, 'login.html', {'form':form})


