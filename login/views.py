from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import calendar
from .models import UserProfile
from django.http import HttpResponse
import json
import datetime


# Create your views here.

def login(request):
    try:
        if request.method == "GET":
            email = request.META["HTTP_USER"]
            password = request.META["HTTP_PASSWORD"]
            ob = UserProfile.objects.filter(emails=email, password=password)
            if ob.exists():
                return HttpResponse(json.dumps({"message": "success"}))
            else:
                return HttpResponse("LOgi failed")
    except TypeError:
        return HttpResponse("Error")


@csrf_exempt
def profiledisplay(request):
    if request.method == "GET":
        username = request.META["HTTP_USER"]
        password = request.META["HTTP_PASSWORD"]
        ob = UserProfile.objects.filter(emails=username, password=password)[0]
        dic = {"name": ob.name, "dob": str(ob.dob), "emails": ob.emails, "adress": ob.adress}
        j = json.dumps(dic)
        return HttpResponse(j)


@csrf_exempt
def insert(request):
    if request.method == "POST":
        body = request.body.decode("UTF-8")
        j = json.loads(body)
        name = j["name"]
        password = j['password']
        dob = (j["dob"])
        emails = j['emails']
        adress = j['adress']
        dob = dob.split("/")
        print(dob)
        year = int(dob[0])
        month = int(dob[1])
        day = int(dob[2])
        # datetime.date(year, month, day)
        ob = UserProfile(name=name, password=password, dob=datetime.datetime.now(), emails=emails, adress=adress)
        j = ob.save(force_insert=True)
        return HttpResponse(json.dumps({"message": "successfully registered"}))
@csrf_exempt
def update(request):
    if request.method=="POST":
        header=request.META["HTTP_USER"]
        body=request.body.decode("UTF-8")
        j=json.loads(body)
        name=j["name"]
        adress=j["adress"]
        ob=UserProfile(name=name,adress=adress)
        j=UserProfile.objects.filter(emails=header).update(name=name,adress=adress)
        return HttpResponse(json.dumps({"message":"updated Successfully"}))

