from django.shortcuts import render, HttpResponseRedirect
from tickets.models import Ticket
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from users.forms import UserLogin, UserRegistration, UserProfile


def Login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('Profile'))
    else:
        form = UserLogin()
    context = {
        "current_url": reverse('Login'),
        'form': form
    }
    return render(request, 'users/Login.html', context)


def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('Home_page'))


def Registration(request):
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful registration!')
            return HttpResponseRedirect(reverse('Login'))
    else:
        form = UserRegistration()
    context = {
        "current_url": reverse('Registration'),
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@login_required
def Profile(request):
    if request.method == 'POST':
        form = UserProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Profile'))
    else:
        form = UserProfile(instance=request.user)

    context = {
        "current_url": reverse('Profile'),
        'form': form,
    }
    return render(request, 'users/profile.html', context)

