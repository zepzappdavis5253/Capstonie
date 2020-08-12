import requests
import json
import django.contrib.auth
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Instrument, Score
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User





def index(request):
    return render(request, 'drumbeatapp/index.html')


def get_instruments(request):
    instruments = Instrument.objects.all()
    data = []
    for instrument in instruments:
        data.append({
            'id': instrument.id,
            'name': instrument.name,
            'sound': instrument.sound,
        })
    return JsonResponse({'instruments': data})


def get_scores(request):
    scores = Score.objects.all().filter(user=request.user)
    data = []
    for score in scores:
        print(json.loads(score.score_data))
        score_data = json.loads(score.score_data)
        data.append(score_data)
    return JsonResponse({'scores': data})


def save_score(request):
    data = json.loads(request.body)
    data = json.loads(data["score"])
    name = data["score_name"]
    # if name == '':
    #     return HttpResponse('not ok')
    score = Score(name=name, score_data=json.dumps(data), user=request.user)
    score.save()
    return HttpResponse("ok")


def login_register(request):
    return render(request, 'drumbeatapp/login_register.html')


def login_page(request):
    return render(request, 'drumbeatapp/login.html')


def register_page(request):
    return render(request, 'drumbeatapp/register.html')


@login_required
def protected(request):
    score_name = request.POST['score_name']
    return render(request, 'drumbeatapp/index.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = django.contrib.auth.authenticate(request, username=username, password=password)
    if user is None: # authenticiation failed, send them back to the login/register page
        print("User was None, redirecting")
        return HttpResponseRedirect(reverse('drumbeatapp:login_page'))
    # authentication succeeded, send them to the protected page
    django.contrib.auth.login(request, user)
    return HttpResponseRedirect(reverse('drumbeatapp:index'))


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    django.contrib.auth.login(request, user)
    return HttpResponseRedirect(reverse('drumbeatapp:index'))


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('drumbeatapp:login_page'))
