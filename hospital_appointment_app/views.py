from hospital_appointment_app.models import Appointment
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from hospital_appoinment_project import settings
from django.contrib.auth.decorators import login_required, user_passes_test




from .forms import NewUserForm, AppointmentForm

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

#@login_required(login_url='login')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment')

    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form' : form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homepage')
        messages.error(request, "Unsuccessful registration. Invalid format.")
    else:
        form = NewUserForm()
    return render(request=request, template_name ='register.html', context={'form':form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('appointment')
            else:
                messages.error(request, 'Invalid Username Or Password')
        else:
            messages.error(request, 'Invalid Username or password')

    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={'form':form})

def logout_request(request):
    logout(request)
    #message.info(request,"you will have successfully loggedout.")
    return redirect("login_request")

def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_user = User.objects.get(email=data)
            if associated_user:
                subject = 'Password Reset Requested'
                email_template_name = 'password_reset_email.txt'
                c = {
                    'email':associated_user.email,
                    'domain': '127.0.0.1:8000',
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'site' : 'Demo Website',
                    'user': associated_user,
                    'token': default_token_generator.make_token(associated_user),
                    'protocal':'http',
                }
                email = render_to_string(email_template_name, c)
                send_mail(subject, email, 'setting.EMAIL_HOST_USER', [associated_user.email], fail_silently=False)
                return redirect('/password_reset/done/')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='password_reset.html', context={'password_reset_form':password_reset_form})