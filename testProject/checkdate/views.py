from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "checkdate/index.html", {
        "date": now.month == 6 and now.day == 10,
    })
    

