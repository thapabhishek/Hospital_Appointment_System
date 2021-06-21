from collections import namedtuple
from re import template
from django.contrib.auth import logout
from django.urls import path
from django.urls.resolvers import URLPattern

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('register/', views.register, name='register'),
    path('appointment/', views.appointment, name='appointment'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]