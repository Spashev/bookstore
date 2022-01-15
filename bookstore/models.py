from django.db import models
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify, truncatechars


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    label = models.ImageField(upload_to='books/%Y/%m/%d')
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)
    soft_deleted = models.BooleanField(default=False)
    genre = models.ManyToManyField('Genre', blank=True)
    viewers = models.IntegerField(default=1, editable=False)
    likes = models.IntegerField(default=0, editable=False)
    file = models.FileField(upload_to='books/files/%Y/%m/%d', null=True, blank=True, help_text='Файл(книга)')
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
    @property
    def short_description(self):
        return truncatechars(self.description, 35)
    
    @property
    def get_description(self):
        return truncatechars(self.description, 400)
    
    def get_absolute_url(self):
        return reverse_lazy('bookstore:books', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def addViewers(self, *args, **kwargs):
        self.viewers += 1
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ('-created',)
        

class Author(models.Model):
    name = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255, help_text='Полная И.Ф.О')
    soft_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.fullname})'
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    

class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Жанр')
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse_lazy('bookstore:genres', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
