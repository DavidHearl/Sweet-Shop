from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required()
def user_profile(request):
    """ View for the user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update Failed!, Please ensure the form is \
                           correct and there are no missing fields')
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

    template = 'profiles/user_profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required()
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'An Email for The past order confirmation: \
        { order_number } was sent on the date of order'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
