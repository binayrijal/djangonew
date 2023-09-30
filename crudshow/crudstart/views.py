from django.shortcuts import render
from .form import UserRegistration
from.models import User
from django.http import HttpResponseRedirect,HttpResponse

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


