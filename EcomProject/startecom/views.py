from django.shortcuts import render

def index(request):
    return render(request,'startecom/index.html') #this is main home function to call


def contact(request):
    return render(request,'startecom/contact.html')