from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'Account.html')


def aboutus(request):
    return render(request, 'AboutUs.html')