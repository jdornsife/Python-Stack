from django.utils.crypto import render, HttpResponse, redirect, get_random_string
  
def index(request):
    unique_id = get_random_string(length= 14)
    
return index()



