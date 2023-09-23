from django.shortcuts import render
from .form import UserRegistration
from.models import User

# Create your views here.
def addshow(request):
    if request.method=="POST":
        fo=UserRegistration(request.POST)
        if fo.is_valid():
            fo.save()
            fo=UserRegistration()
    else:
        fo=UserRegistration()
        userdata=User.objects.all()
        
    return render(request,'addandshow.html',{'fobj':fo})