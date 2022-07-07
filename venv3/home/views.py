from django.shortcuts import render
from django.http import HttpResponse

def viewOne(request):
    return render( request,'home/welcome.html',{})