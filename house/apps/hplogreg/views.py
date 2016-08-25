from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User

def index(request):
    return render(request, 'hplogreg/index.html')

def register(request): #just taking the request object
    user = User.objects.register(request.POST) #user = a tuple, 2 options, (True, user) or (False, errors)
    if user[0]:
        request.session['user'] = {
            'id':user[1].id,
            'name':user[1].name,
            'email':user[1].email,
        }
        return redirect(reverse('house:index'))
    #build flash messages here using user[1]
    for error in user[1]: #always going to be referring as user 1 because it's the first user in the list
        messages.error(request, error)
    return redirect(reverse('hplog:index'))

def login(request):
    user = User.objects.login(request.POST)
    if user[0]:
        request.session['user'] = {
            'id':user[1].id,
            'name':user[1].name,
            'email':user[1].email,
        }
        return redirect(reverse('house:index')) #what this does here is when the log in is successful, it will redirect the user to the home page of the bookreview app
 #flash messages
    for error in user[1]:
        messages.error(request, error)
    return redirect(reverse('hplog:index'))

def logoff(request):
    request.session.clear()
    return redirect(reverse('hplog:index'))
