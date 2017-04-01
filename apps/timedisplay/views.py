from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    i = datetime.datetime.now()
    date = i.strftime("%b %d, %Y")
    time = i.strftime("%I:%M %p")
    context = {
        "date": date,
        "time": time
    }

    return render(request, "timedisplay/index.html", context)
