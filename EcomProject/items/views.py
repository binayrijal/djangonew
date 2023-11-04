from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Items,Category
from items.forms import NewItemForm
from django.shortcuts import redirect

def details(request,pk):
    items=get_object_or_404(Items,pk=pk)
    related_items=Items.objects.filter(Category=items.Category,is_sold=False).exclude(pk=pk)
    return render(request,'items/detail.html',
    {
     'items':items,
     'related_items':related_items
    }
    )

@login_required
def new(request):
    if request.method=="POST":
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('items:details', pk=item.id)
    else:
        form=NewItemForm()
    return render(request,'items/form.html',{
      'form':form, 
      'title':'New item',
    })
