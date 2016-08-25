from django.shortcuts import render, HttpResponse, redirect, reverse
import random
# Create your views here.
def index(request):
    return render(request, "harry_app/index.html")

# Create your views here.
def lockhart(request):
    if "total" not in request.session:
        request.session["total"] = 0
    if "log" not in request.session:
        request.session["log"] = []
    return render(request, "harry_app/lockhart.html")

def process(request):
    userhp = 100;
    lockhartattack = random.randint(5, 10)
    if request.method == "POST":
        if request.POST["spell"] == "flee":
            return redirect('duel:index')

        elif request.POST["spell"] == "heal":
            healNum = random.randint(5, 10)
            request.session["total"] += healNum
            request.session["log"].append("You healed " + str(healNum) + " to your total HP!")

        elif request.POST["spell"] == "attack":
            attackNum = random.randint(2, 5)
            request.session["total"] += attackNum
            request.session["log"].append("Expelliarmus hits for " + str(attackNum) + " damage!")

        elif request.POST["spell"] == "chance":
            chanceNum = random.randint(-50, 50)
            if chanceNum < 0:
                request.session["log"].append("Expulso blew up in your face! You lost " + str(chanceNum) + " hp!")
                request.session["total"] += chanceNum
            else:
                request.session["log"].append("Expulso was a success, " + str(chanceNum) + " damage done!")
                request.session["total"] += chanceNum
    request.session["log"].append("Lockhart casts Obliviate on you for " + str(lockhartattack) + " damage!")
    if userhp == 0:
        return redirect(reverse('duel:index'))
    return redirect(reverse('duel:lockhart'))


def clear(request):
    request.session.clear()
    return redirect('duel:index')
