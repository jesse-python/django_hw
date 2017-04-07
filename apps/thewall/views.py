from django.shortcuts import render, redirect
from django.contrib import messages
from django_hw.thewall.forms import RegisterForm
from django.views.generic import View
from django.contrib.auth import login, authenticate, forms, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
# def index(request):
#     return render(request, "the_wall/index.html")

# def register(request, methods=['POST']):
#     print 'working'
#     print request.POST
#
#
#     return redirect('/the_wall')
#
# def login(request, methods=['POST']):
#     pass

class Register(View):
    form = RegisterForm
    def get(self, request):
        context = {'form': self.form()}
        return render(request, 'users/register.html', context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/login.html')
        else:
            context = {'form': form}
            return render(request, 'users/register.html', context)

class Login(View):
    form = forms.AuthenticationForm
    def get(self, request):
        context = {'form': self.form()}
        return render(request, 'users/login.html', context)
    def post(self, request):
        form = self.form(None, request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/wall')
            else:
                return render(request, 'users/login.html', context)
        else:
            return render(request, 'users/login.html', context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')
