from django.shortcuts import redirect, render, reverse, HttpResponse


def view_shopping_bag(request):
    """ A view to return the contents of the shopping bag/basket """
    
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ A view to add the quanity to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list (shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity
    
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def modify_shopping_bag(request, item_id):
    """ A view to modify the contents of the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)
    
    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """ A view remove an item from the shopping bag"""

    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return HttpResponse(status=200)