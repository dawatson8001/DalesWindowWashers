# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from Accounts_app.forms import UserRegistrationForm, UserLoginForm, PersonalDetailsForm
from django.contrib.auth.decorators import login_required
from .models import User


def register(request):
    if User.objects.filter(username=request.username).exists():
        messages.error(request, "Email already in use!")
        return render(request, 'register.html')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return render(request, 'account.html', {'form': form})

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return render(request, 'index.html')
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


@login_required
def account_details(request):
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            form.save()
    else:

        form = PersonalDetailsForm()

    args = {
        'form': form,
    }
    args.update(csrf(request))

    return render(request, 'account.html', args)
