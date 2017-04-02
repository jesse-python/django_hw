from django.shortcuts import render, redirect
import random, string
# Create your views here.

def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0

    randword = ""
    for i in range(0,14):
        randletter = random.choice(string.letters)
        print randletter
        randword += randletter

    request.session['attempt'] += 1

    context = {
       'randword': randword,
       'attempt': request.session['attempt']
    }
    return render(request, "randword/index.html", context)

def generateWord(request):

    redirect('/randword')
