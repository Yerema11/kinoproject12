from django.contrib import admin
from .models import Post
from .models import Movie, Ticket

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'created_at', 'image')  # Добавляем изображение в список
    list_filter = ('post_type',)  # Фильтры по типу поста
    search_fields = ('title', 'content')  # Возможность поиска по заголовку и контенту
    fields = ('title', 'content', 'post_type', 'image')  # Поля в форме

    @admin.register(Movie)
    class MovieAdmin(admin.ModelAdmin):
        list_display = ('title', 'release_date', 'rating')
        search_fields = ('title',)

    # Регистрация модели Ticket
    @admin.register(Ticket)
    class TicketAdmin(admin.ModelAdmin):
        list_display = ('movie_name', 'user', 'session_time', 'seat_number')
        list_filter = ('user', 'session_time')

admin.site.register(Post, PostAdmin)
