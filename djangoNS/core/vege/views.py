from django.shortcuts import render
from .models import *
def receipe(request):
    if(request.method=='POST'):
        data=request.POST
        print(type(data))
    
    return render(request,"receipe.html")
