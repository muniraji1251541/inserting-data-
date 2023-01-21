from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def fi(request):
    sn=input('Enter Sport Name: ')
    t=Sport.objects.get_or_create(sport_name=sn)[0]
    t.save()
    return HttpResponse('Sport is added successfully.')

def si(request):
    sn=input('Enter Sport Name: ')
    name=input('Enter Player Name: ')
    url=input('Enter Player URL: ')
    t=Sport.objects.get_or_create(sport_name=sn)[0]
    t.save()
    w=Player.objects.get_or_create(sport_name=t,name=name,url=url)[0]
    w.save()
    return HttpResponse('Player is added successfully.')

def ti(request):
    name=input('Enter Player Name: ')
    date=input('Enter Date: ')
    w=Player.objects.get_or_create(name=name)[0]
    w.save()
    d=Detail.objects.get_or_create(name=w,date=date)[0]
    d.save()
    return HttpResponse('Details of palyers added successfully.')
