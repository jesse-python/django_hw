from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def allninjas(request):
    return render(request, 'disappearing_ninjas/allninjas.html')

def showninja(request, ninja_color):
    print "working"
    print ninja_color
    context = {
        'ninja_color': ninja_color
    }

    return render(request, 'disappearing_ninjas/showninja.html', context)
