from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(featured=True)
    carousel_list = []
    featured_count = []

    for product in products:
        featured_count.append(product)
        if len(featured_count) == 4:
            carousel_list.append(featured_count[:])
            featured_count.clear()

    context = {
        'carousel_list': carousel_list,
        'featured_count': featured_count,
        'products': products,
    }

    return render(request, 'home/index.html', context)
