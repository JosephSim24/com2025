from django.urls import path
from . import views
from .views import add_song

urlpatterns = [
    # ex: /albums/
    path('', views.index_albums, name='index'),
    # ex: /albums/:id/
    path('<int:album_id>/', views.show_album, name='show_album'),
    # ex: /albums/new/
    path('new/', views.new_album, name='new_album'),
    #ex: /albums/:id/add-song/
    path('<int:album_id>/add-song/', views.add_song, name="add_song"),
    #ex: /albums/:id/delete/
    path('<int:album_id>/delete/', views.delete_view, name="delete_view"),
]
