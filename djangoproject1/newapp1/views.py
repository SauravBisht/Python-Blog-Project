from django.http import HttpResponse
import datetime
from django.shortcuts import render

def index (request):
    return HttpResponse("Hello, world! You are at myapp1.Index Page")


def home (request):
    return HttpResponse("This is a Home Page")

def hello (request):
    text="""<h1> Welcome to my page <h1>"""
    return HttpResponse(text)

def today (request):
    today= datetime.datetime.now().date()
    daysofweek =['Mon','Tue','Wed','Thr','Fri','Sat','Sun']
    return render(request,"newapp1/temp1.html",{"today":today ,"days_of_week" : daysofweek})

def saurav (request):
    today= datetime.datetime.now().date()
    daysofweek =['Mon','Tue','Wed','Thr','Fri','Sat','Sun']
    return render(request,"newapp1/saurav.html",{"today":today ,"days_of_week" : daysofweek})