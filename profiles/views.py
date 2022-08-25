from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': user_profile
    }

    return render(request, template, context)
