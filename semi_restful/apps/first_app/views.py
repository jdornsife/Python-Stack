from django.shortcuts import render, HTTPResponse,redirect


def index(request):
    response = "hello, I am your first request"
    return render(request)

# Create your views here.
