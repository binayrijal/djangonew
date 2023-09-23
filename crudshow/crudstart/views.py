from django.shortcuts import render

# Create your views here.
def add_show(request):
    return render(request,'base.html')
def addshow(request):
    return render(request,'addandshow.html')