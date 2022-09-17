from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    featured_count = 0
    featured = 0

    if request.GET:
        for product in products:
            if product.featured:
                featured_count += 1

            return featured_count

    # context['featured'] = range[1,3]

    context = {
        'loop_times' : range(1,3),
        'featured_count': featured_count,
        'featured': featured,
        'products': products,
    }

    return render(request, 'home/index.html', context)
