from django.urls import path
from . import views

urlpatterns = [
    # ex: /albums/
    path('', views.index_albums, name='index'),
    # ex: /albums/:id/
    path('<int:album_id>/', views.show_album, name='show_album'),
    # ex: /albums/new/
    path('new/', views.new_album, name='new_album'),
]
