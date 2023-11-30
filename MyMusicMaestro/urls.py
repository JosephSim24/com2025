from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #ex: /
    path('', include('app_pages.urls')),
    #ex: /albums/
    path('albums/', include('app_album_viewer.urls')),
    #ex: /admin/
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
