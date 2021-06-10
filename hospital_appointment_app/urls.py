from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('register/', views.register, name='register'),
    path('appointment/', views.appointment, name='appointment'),
    path('login/', views.login_request, name='login_request'),
]