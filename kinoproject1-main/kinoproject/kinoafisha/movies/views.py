from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Movie, Ticket
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from .forms import MovieSearchForm  # Импортируем форму для поиска фильмов


def movie_list(request):
    # Получаем все фильмы
    movies = Movie.objects.all()

    # Обработка поискового запроса
    form = MovieSearchForm()
    if 'query' in request.GET:
        form = MovieSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            movies = movies.filter(title__icontains=query)  # Фильтруем фильмы по названию

    return render(request, 'movies/movie_list.html', {'movies': movies, 'form': form})


@login_required
def buy_ticket(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Присваиваем билет текущему пользователю
            ticket.save()  # Сохраняем билет в базе данных
            return redirect('my_tickets')  # Перенаправляем на страницу с билетами
    else:
        form = TicketForm(initial={'movie_name': movie.title})  # Предзаполняем фильм

    return render(request, 'buy_ticket.html', {'form': form, 'movie': movie})


@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)  # Получаем билеты текущего пользователя
    return render(request, 'my_tickets.html', {'tickets': tickets})


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})


# Вход
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'movies/login.html', {'form': form})


# Выход
def logout_view(request):
    logout(request)
    return redirect('index')


# Главная страница
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # Получаем все посты
    return render(request, 'movies/index.html', {'posts': posts})
