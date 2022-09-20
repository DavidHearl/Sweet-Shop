from django.shortcuts import get_object_or_404, redirect, render, \
    reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_shopping_bag(request):
    """ A view to return the contents of the shopping bag/basket """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ A view to add the quanity to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {shopping_bag[item_id]}')
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def modify_shopping_bag(request, item_id):
    """ A view to modify the contents of the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {shopping_bag[item_id]}')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """ A view remove an item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return HttpResponse(status=200)
