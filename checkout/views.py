from django.shortcuts import get_object_or_404, redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shopping_bag.contexts import shopping_bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in shopping_bag.items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with this form \
                Please ensure that the information entered is correct')
                
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_shopping_bag = shopping_bag_contents(request)
        total = current_shopping_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is not set.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_completed_successfully(request, order_number):
    """"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order processed successfully! \
        We hope you enjoy your order. See important order details below. \
        Your Order Number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
