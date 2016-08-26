from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from ..hplogreg.models import User

def index(request):

    return render(request, "house_app/all_houses.html")

def gryffindor(request):

    return render(request, "house_app/gryffindor.html")

def hufflepuff(request):

    return render(request, "house_app/hufflepuff.html")

def ravenclaw(request):

    return render(request, "house_app/ravenclaw.html")

def slytherin(request):

    return render(request, "house_app/slytherin.html")
