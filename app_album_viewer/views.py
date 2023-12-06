from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Album, Comment, Song
from django.shortcuts import get_object_or_404
from django.db.models import Count
from datetime import date

def index_albums(request):
    #retreive all albums from the db and annotate each with a comment count
    all_albums = Album.objects.annotate(comment_count=Count('comments')).order_by('title')

    #create a dictionary to store this data
    context = {'albums': all_albums} 

    #render the page
    return render(request, 'app_album_viewer/index.html', context)

def show_album(request, album_id):
    #retreive all albums and its respective comments and songs from the db
    album = get_object_or_404(Album, pk=album_id)
    comments = Comment.objects.filter(album=album)
    songs = Song.objects.filter(albums=album)

    #create a dictionary to store the data
    context = {'album': album, 'comments': comments, 'songs': songs}

    #render the page
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
            release_date=date(release_date))
        album.save()

        return HttpResponseRedirect('/app_album_viewer/')

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'app_album_viewer/new.html', {})
