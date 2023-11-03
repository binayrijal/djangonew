from django.shortcuts import render

def index(request):
    return render(request,'startecom/index.html')


def contact(request):
    return render(request,'startecom/contact.html')