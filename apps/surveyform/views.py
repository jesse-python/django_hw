from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
    return render(request, 'surveyform/index.html')

def process(request):

    request.session['attempt'] += 1

    request.session['name'] = request.POST.get('name')
    request.session['dojoloc'] = request.POST.get('dojoloc')
    request.session['favlang'] = request.POST.get('favlang')
    request.session['comment'] = request.POST.get('comment')

    return redirect('/surveyform/result')

def result(request):

    return render(request, 'surveyform/result.html')
