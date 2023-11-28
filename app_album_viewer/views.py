from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

def index_albums(request):
    return HttpResponse("We are in the index albums view")

def show_album(request, album_id):
    return HttpResponse("We are in the show album view for album"
                        + str(album_id))

def new_album(request):
    return HttpResponse("We are in the new album view")
