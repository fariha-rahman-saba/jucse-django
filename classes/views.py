from django.shortcuts import render
from .models import Classes


def home(request):
    clas = Classes.objects
    return render(request,'classes/home.html',{'clas':clas})

def addclasses(request):
    return render(request,'classes/add_classes.html')