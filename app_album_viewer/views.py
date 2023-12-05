from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Album
from django.shortcuts import get_object_or_404
from django.db.models import Count

def index_albums(request):
    #retreive all albums from the db and annotate each with a comment count
    all_albums = Album.objects.annotate(comment_count=Count('comments')).order_by('title')

    #create a dictionary to store this data
    context = {'albums': all_albums} 

    #render the page
    return render(request, 'app_album_viewer/index.html', context)

def show_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'app_album_viewer/show.html', context)

def new_album(request):
    if request.method == 'POST':
        title = request.POST.get("Title", "")
        artist = request.POST.get("Artist", "")
        price = request.POST.get("Price", "")
        cover = request.POST.get("Cover", "")
        description = request.POST.get("Description", "")
        format = request.POST.get("Format", "")
        release_date = request.POST.get("Release_Date", "")
        # create a form instance and populate it with data from the request:
        album = Album(title=title, artist=artist, price=price, 
            cover=cover, description=description, format=format,
            release_date=release_date)
        album.save()

        return HttpResponseRedirect('/app_album_viewer/')

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'app_album_viewer/new.html', {})

def test(request):
    return render(request, 'app_album_viewer/test.html', {})