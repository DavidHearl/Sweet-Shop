from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ModifyProductsForm, ReviewForm


def all_products(request):
    """ A view to return all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'color' in request.GET:
            color = request.GET['color'].split(',')
            products = products.filter(color__in=color)

        if 'flavour' in request.GET:
            flavour = request.GET['flavour'].split(',')
            products = products.filter(flavour__in=flavour)

        if 'brand' in request.GET:
            brand = request.GET['brand'].split(',')
            products = products.filter(brand__in=brand)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No Search Criteria Present")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(active=True)
    review_form = None
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.username = request.user
            new_review.product = product
            new_review.save()
        else:
            review_form = ReviewForm() 

    context = {
        'product': product,
        'review': reviews,
        'new_review': new_review,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required()
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    logged_user = request.user.id

    review.delete()
    messages.success(request, f"Your review has been removed")

    return redirect(reverse('product/product_detail.html'))


@login_required()
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This function is only available for superusers')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ModifyProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Product Added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Product could not be created, Please ensure the \
                           form is correct and there are no missing fields')
    else:
        form = ModifyProductsForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def modify_product(request, product_id):
    """ Modify a product in the database """
    if not request.user.is_superuser:
        messages.error(
            request, 'This function is only available for superusers')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ModifyProductsForm(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Product could not be modified, Please ensure the \
                           form is correct and there are no missing fields')
    else:
        form = ModifyProductsForm(instance=product)
        messages.info(request, f'{product.name} is being modified')

    template = 'products/modify_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    """ Modify a product in the database """
    if not request.user.is_superuser:
        messages.error(
            request, 'This function is only available for superusers')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect(reverse('products'))
