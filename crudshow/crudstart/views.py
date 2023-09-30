from django.shortcuts import render,redirect
from .form import UserRegistration
from.models import User,Teacher
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication

# Create your views here.
def addshow(request):
    if request.method=='POST':
        fo=UserRegistration(request.POST)
        if fo.is_valid():
            fo.save()
            fo=UserRegistration()
    else:
        fo=UserRegistration()
    
    
    regr=User.objects.all()
        
    return render(request,'addandshow.html', {'fobj':fo,'regs':regr} )

def delete_data(request,id):
    if request.method=='POST':
        obj=User.objects.get(pk=id)
        obj.delete()
    return HttpResponseRedirect('/')


def update_data(request,id):
   
    if request.method=='POST':
        obj=User.objects.get(pk=id)
        fm=UserRegistration(request.POST,instance=obj)
        if fm.is_valid():
          fm.save()
          return render(request,'addandshow.html')
    else:
        obj=User.objects.get(pk=id)
        fm=UserRegistration(instance=obj)
    
    return render(request,'updata.html',{'fmdata':fm})

def form_show(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        check=request.POST.getlist('checkbox')
        if "on" in check:
            check=True
        else:
            check=False
        exist_teacher= Teacher.objects.filter(email=email).first()
        if not exist_teacher:
            hash_password=make_password(password) 
            new_teacher=Teacher.objects.create(email=email,password=hash_password,checkbox=check)
            new_teacher.save()
            return redirect(request,'token.html',{'new':new_teacher})
        else:
           return render(request,'form.html',{'message':'username is taken'})
    return render(request,'form.html',{'message':'this is not allowed'})
    
def gettoken(request):
 if request.method=="POST":
     pass
    