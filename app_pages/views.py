from django.shortcuts import render
from app_album_viewer.models import Album
from django.shortcuts import get_object_or_404


def home_page(request):
    #render the home page
    return render(request, 'app_pages/home_page.html', {})

def contact_page(request):
    #render the contact page
    return render(request, 'app_pages/contact_page.html', {})

def about_page(request):
    #render the about page
    return render(request, 'app_pages/about_page.html', {})

def account_page(request):
    #render the user's account details
    return render(request, 'app_pages/account_page.html', {})

def login_page(request):
    #render the login page
    return render(request, 'app_pages/login.html', {})

def recommend_page(request):
    #Retreives the album with the specified id
    album_id = request.GET.get('album')

    #Stores the album or a 404 error is thrown
    if album_id is not None:
        album = get_object_or_404(Album, pk=album_id)
    else:
        return render(request, '404.html', status=404)
    context = {'album': album}

    #renders the recommend a friend page for that album
    return render(request, 'app_pages/recommend_page.html', context)

