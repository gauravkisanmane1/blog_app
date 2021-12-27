from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_app.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
