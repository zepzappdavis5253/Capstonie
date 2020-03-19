from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .models import Instrument

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