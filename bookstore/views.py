from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book, Genre
from django.http import Http404
from django.utils import timezone


class MainView(TemplateView):
    template_name='home/main.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genres'] = Genre.objects.all()[:6]
        
        return context


class GenreView(TemplateView):
    template_name='book/books.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genre'] = Genre.objects.get(slug=kwargs.get('slug', None), status=True)
        context['books'] = context['genre'].book_set.all()
        
        return context


class BookView(DetailView):
    model = Book
    template_name='book/details.html'
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        try:
            book = Book.objects.get(slug=slug)
            book.addViewers()
            return book
        except Exception:
            raise Http404('Ох, нет объекта;)')
    

class BookListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'book/books.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

