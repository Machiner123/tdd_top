from django.shortcuts import redirect, render
#from django.http import HttpResponse
from lists.models import Item



def home_page(request):
    '''
    check if request is POST, if yes create Item object with text == item_text, redirect
    to homepage. whether post or not, store all created Item objects in item, render 
    home.html, with {% items %} python object in for loop being replaced the list of
    objects in var items
    '''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
