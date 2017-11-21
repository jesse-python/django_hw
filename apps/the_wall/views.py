# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import User, Message, Comment
import re
from django.http import HttpResponseRedirect

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# Create your views here.

def index(request):
    return render(request, 'the_wall/index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    bool = True
    flashes = []

    if not email:
        flashes.append('Email cannot be blank')
        bool = False
    elif not EMAIL_REGEX.match(email):
        flashes.append('Email must be valid, try again')
        bool = False

    if not password:
        flashes.append('Password cannot be blank')
        bool = False

    if bool:
        user_query = User.objects.filter(email=email).first()
        if password == user_query.password:
            print('Logged in!')
            request.session['userid'] = user_query.id
            request.session['f_name'] = user_query.first_name
            return render(request, 'the_wall/dashboard.html')
    else:
        flashes.append('Password was incorrect')
        return render(request, 'the_wall/index.html')

    return render(request, 'the_wall/index.html')

def register(request):
    print ('working')

    print (request.POST)

    print (request.POST['l_name'])

    email = request.POST['email']
    password = request.POST['password']
    f_name = str(request.POST['f_name'])
    l_name = str(request.POST['l_name'])
    c_password = request.POST['c_password']

    bool = True
    flashes = [];

    if not f_name:
        flashes.append("First Name cannot be blank")
        bool = False
    elif len(f_name) < 2:
        flashes.append("First name must be greater than 2 characters")
        bool = False
    elif not str.isalpha(f_name):
        flashes.append("First name must not contain non-alphabetic characters")
        bool = False

    if not l_name:
        flashes.append("Last Name cannot be blank")
        bool = False
    elif len(l_name) < 2:
        flashes.append("Last name must be greater than 2 characters")
        bool = False
    elif not str.isalpha(l_name):
        flashes.append("Last name must not contain non-alphabetic characters")
        bool = False

    if not email:
        flashes.append("Email must not be blank")
        bool = False
    elif not EMAIL_REGEX.match(email):
        flashes.append('Email must be valid, try again')
        bool = False

    if not password:
        flashes.append("Password must not be blank")
        bool = False
    elif len(password) < 8:
        flashes.append("Password must be greater than 8 characters")
        bool = False

    if not c_password:
        flashes.append("Password confirmation must not be blank")
        bool = False
    elif password != c_password:
        flashes.append("password must be the same as password confirmation")
        bool = False

    if bool:
        newuser = User(first_name=f_name, last_name=l_name, email=email, password=password)
        newuser.save()

        getuser = User.objects.get(email=email)
        request.session['userid'] = getuser.id
        request.session['f_name'] = getuser.first_name


        return render(request, 'the_wall/dashboard.html')

    context = {
        'errors': flashes,
    }

    print(flashes)

    return render(request, 'the_wall/index.html', context)




def dashboard(request):

    return render(request, 'the_wall/dashboard.html')
