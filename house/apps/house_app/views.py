from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    print '%%%%%%%%%% You are on the sorting page %%%%%%%%%%'

    return render(request, "house_app/all_houses.html")

def gryffindor(request):
    print '%%%%%%%%%% You are on the gryffindor page %%%%%%%%%%'

    return render(request, "house_app/gryffindor.html")

def hufflepuff(request):
    print '%%%%%%%%%% You are on the hufflepuff page %%%%%%%%%%'

    return render(request, "house_app/hufflepuff.html")

def ravenclaw(request):
    print '%%%%%%%%%% You are on the ravenclaw page %%%%%%%%%%'

    return render(request, "house_app/ravenclaw.html")

def slytherin(request):
    print '%%%%%%%%%% You are on the slytherin page %%%%%%%%%%'

    return render(request, "house_app/slytherin.html")
