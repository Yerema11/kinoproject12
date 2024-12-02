from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['session_time', 'seat_number']  # Даем пользователю заполнить время сеанса и место

class MovieSearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск фильмов',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите название фильма'})
    )
