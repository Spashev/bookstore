from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('genre/<slug:slug>', views.GenreView.as_view(), name='genres'),
    path('book/<slug:slug>', login_required(views.BookView.as_view()), name='books'),
    path('books', views.BookListView.as_view(), name='books_list'),
]
