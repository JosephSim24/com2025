from django.urls import path
from . import views

urlpatterns = [
    # ex: /app_album_viewer/
    path('', views.index_albums, name='index'),
    # ex: /app_album_viewer/1/
    path('<int:album_id>/', views.show_album, name='show_album'),
    # ex: /app_album_viewer/new/
    path('new/', views.new_album, name='new_album'),
]
