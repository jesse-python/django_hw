from django.shortcuts import render, redirect
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
def index(request):
    return render(request, "the_wall/index.html")

def register(request, methods=['POST']):
    print 'working'
    print request.POST

    


    return redirect('/the_wall')

def login(request, methods=['POST']):
    pass
