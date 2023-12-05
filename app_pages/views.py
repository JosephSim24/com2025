from django.shortcuts import render


def home_page(request):
    return render(request, 'app_pages/home_page.html', {})

def contact_page(request):
    return render(request, 'app_pages/contact_page.html', {})

def about_page(request):
    return render(request, 'app_pages/about_page.html', {})

def account_page(request):
    return render(request, 'app_pages/account_page.html', {})