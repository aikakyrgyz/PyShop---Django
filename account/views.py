from django.shortcuts import render
from django.contrib.auth.views  import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.urls import reverse_lazy

# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')


