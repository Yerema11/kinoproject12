
from django.contrib import admin
from django.urls import path, include  # Добавляем include для подключения urls приложений
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),  # Подключаем urls приложения movies
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
