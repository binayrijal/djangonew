from django.shortcuts import render
from items.models import Items,Category

def index(request):
    items=Items.objects.filter(is_sold=False)[0:6] #it shows only five items matching
    category=Category.objects.all()
    return render(request,'startecom/index.html',
                  {
                   'items':items,
                   'category':category,
                   })                               #this is main home function to call


def contact(request):
    return render(request,'startecom/contact.html')