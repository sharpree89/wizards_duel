from django.shortcuts import render, HttpResponse, redirect, reverse
import random
# Create your views here.
def index(request):
    return render(request, "harry_app/index.html")

# Create your views here.
def lockhart(request):
    if "userhp" not in request.session:
        request.session["userhp"] = 100

    if "enemyhp" not in request.session:
        request.session["enemyhp"] = 100

    if "log" not in request.session:
        request.session["log"] = []

    return render(request, "harry_app/lockhart.html")

def potter(request):
    if "myuserhp" not in request.session:
        request.session["myuserhp"] = 100

    if "myenemyhp" not in request.session:
        request.session["myenemyhp"] = 100

    if "mylog" not in request.session:
        request.session["mylog"] = []

    return render(request, "harry_app/potter.html")

def process_potter(request):
    potterattack = random.randint(10, 15)
    myuserhp = request.session["myuserhp"]
    myenemyhp = request.session["myenemyhp"]

    if myuserhp <= 0:
        request.session.clear()
        return redirect(reverse('duel:lose'))
    elif myenemyhp <= 0:
        return redirect(reverse('duel:index'))

    if request.method == "POST":
        if request.POST["spell"] == "flee":
            return redirect('duel:index')

        elif request.POST["spell"] == "heal":
            if request.session["myuserhp"] >= 95 and request.session["myuserhp"] < 100:
                healNum = 1
                request.session["myuserhp"] += healNum
                myuserhp += healNum
                request.session["mylog"].append("You healed " + str(healNum) + " to your total HP!")
            elif request.session["myuserhp"] == 100:
                healNum = 0
                request.session["myuserhp"] += healNum
                myuserhp += healNum
                request.session["mylog"].append("Max health")
            else:
                healNum = random.randint(2, 5)
                request.session["myuserhp"] += healNum
                myuserhp += healNum
                request.session["mylog"].append("You healed " + str(healNum) + " to your total HP!")

        elif request.POST["spell"] == "attack":
            attackNum = random.randint(2, 5)
            request.session["myenemyhp"] -= attackNum
            request.session["mylog"].append("Expelliarmus hits for " + str(attackNum) + " damage!")
            request.session["myuserhp"] -= potterattack
            request.session["mylog"].append("Harry casts Expecto Patronum on you for " + str(potterattack) + " damage!")

        elif request.POST["spell"] == "chance":
            chanceNum = random.randint(-10, 10)
            if chanceNum < 0:
                request.session["mylog"].append("Expulso blew up in your face! You lost " + str(chanceNum) + " hp!")
                request.session["myuserhp"] += chanceNum
            else:
                request.session["mylog"].append("Expulso was a success, " + " Harry takes " + str(chanceNum) + " damage")
                request.session["myenemyhp"] -= chanceNum

    return redirect(reverse('duel:potter'))

def process(request):
    lockhartattack = random.randint(5, 7)
    userhp = request.session["userhp"]
    enemyhp = request.session["enemyhp"]

    if userhp <= 0:
        request.session.clear()
        return redirect(reverse('duel:index'))
    elif enemyhp <= 0:
        return redirect(reverse('duel:potter'))

    if request.method == "POST":
        if request.POST["spell"] == "flee":
            return redirect('duel:index')

        elif request.POST["spell"] == "heal":
            if request.session["userhp"] >= 95 and request.session["userhp"] < 100:
                healNum = 1
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")
            elif request.session["userhp"] == 100:
                healNum = 0
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("Max health")
            else:
                healNum = random.randint(5, 7)
                request.session["userhp"] += healNum
                userhp += healNum
                request.session["log"].append("You healed " + str(healNum) + " to your total HP!")

        elif request.POST["spell"] == "attack":
            attackNum = random.randint(5, 7)
            request.session["enemyhp"] -= attackNum
            request.session["log"].append("Expelliarmus hits for " + str(attackNum) + " damage!")
            request.session["userhp"] -= lockhartattack
            request.session["log"].append("Lockhart casts Obliviate on you for " + str(lockhartattack) + " damage!")

        elif request.POST["spell"] == "chance":
            chanceNum = random.randint(-15, 15)
            if chanceNum < 0:
                request.session["log"].append("Expulso blew up in your face! You lost " + str(chanceNum) + " hp!")
                request.session["userhp"] += chanceNum
            else:
                request.session["log"].append("Expulso was a success, " + " Lockhart takes " + str(chanceNum) + " damage")
                request.session["enemyhp"] -= chanceNum
    return redirect(reverse('duel:lockhart'))

def lose(request):
    return render(request, "harry_app/youlose.html")

def clear(request):
    request.session.clear()
    return redirect('duel:index')
