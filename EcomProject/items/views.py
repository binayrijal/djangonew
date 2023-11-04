from django.shortcuts import render,get_object_or_404
from .models import Items,Category
from items.forms import NewItemForm

def details(request,pk):
    items=get_object_or_404(Items,pk=pk)
    related_items=Items.objects.filter(Category=items.Category,is_sold=False).exclude(pk=pk)
    return render(request,'items/detail.html',
    {
     'items':items,
     'related_items':related_items
    }
    )


def new(request):
    form=NewItemForm()
    return render(request,'items/form.html',{
      'form':form, 
      'title':'New item',
    })
