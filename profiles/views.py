from django.shortcuts import render, get_object_or_404

from .models import User_Profile


def user_profile(request):
    """ View for the user profile """
    profile = get_object_or_404(User_Profile, user=request.user)
    template = 'profiles/user_profiles.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
