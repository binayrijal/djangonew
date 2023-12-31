from django.shortcuts import render,redirect
from .form import UserRegistration
from.models import User,Teacher
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST



# Create your token here.
import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(teacher):
    # Define the payload for the token
    payload = {
        'teacher_id': teacher.id,
        'email': teacher.email,
        'exp': datetime.utcnow() + timedelta(days=1),  # Token expiration time
    }

    # Generate the JWT token
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token





#///



#///

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
            return redirect('addshow')
            
        else:
           return render(request,'form.html',{'message':'message'})
    return render(request,'form.html',{'message':''})

def addshow(request):
     if request.method=='POST':
        fo=UserRegistration(request.POST)
        
        if fo.is_valid():
            hashed_password = make_password(fo.cleaned_data['password'])
            fo = User(name=fo.cleaned_data['name'],email=fo.cleaned_data['email'], password=hashed_password)
            fo.save()
            fo=UserRegistration()
     else:
        fo=UserRegistration()
    
    
     regr=User.objects.all()
        
     return render(request,'addandshow.html', {'fobj':fo,'regs':regr} )
@require_POST
def delete_data(request,id):
    if request.method=='POST':
        obj=User.objects.get(pk=id)
        obj.delete()
    return HttpResponseRedirect('/view')




def update_data(request, id):
    obj = get_object_or_404(User, pk=id)
   
    if request.method == 'POST':
       
        fm = UserRegistration(request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
            return render(request, 'addandshow.html')
    else:
       
        fm = UserRegistration(instance=obj)
    
    return render(request, 'updata.html', {'fmdata': fm})