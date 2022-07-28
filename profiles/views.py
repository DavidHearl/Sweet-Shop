from multiprocessing import context
from re import template
from django.shortcuts import render


def user_profile(request):
    """ View for the user profile """

    template = 'profiles/user_profiles.html'
    context = {}

    return render(request, template, context)
