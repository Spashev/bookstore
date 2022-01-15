from django.contrib import admin
from .models import Book, Author, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'get_authors', 'get_genres', 'soft_deleted']
    list_filter = ('title', 'soft_deleted')
    list_search = ('title', 'get_authors')
    list_per_page = 10
    
    @admin.display(ordering='book__author', description='Author')
    def get_authors(self, obj):
        return obj.author
    
    @admin.display(ordering='book__genre', description='Genres')
    def get_genres(self, obj):
        return "\n".join([genre.title for genre in obj.genre.all()])
    


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'fullname', 'soft_deleted']
    list_filter = ('name', 'soft_deleted')
    list_search = ('name', 'fullname')
    
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ('title', 'status')
    list_search = ('title', )