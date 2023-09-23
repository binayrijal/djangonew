from django.shortcuts import render
from .form import UserRegistration

# Create your views here.
def add_show(request):
    return render(request,'base.html')
def addshow(request):
    if request.method=="POST":
        fo=UserRegistration(request.POST)
    else:
        fo=UserRegistration()
    return render(request,'addandshow.html',{'fobj':fo})