from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    context = {
        "time":"date",
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,"first_app/time_display.html",context)
