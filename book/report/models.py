from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    slug = models.SlugField(unique=True, verbose_name='slug название', null=True)
    title = models.CharField(max_length=100, verbose_name='название категотрии')

    def __str__(self):
        return f'{self.title}'

class Book(models.Model):
     
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    title = models.CharField(max_length=300, verbose_name='заголовок')
    desc = models.TextField(verbose_name='описание')
    date = models.DateField(verbose_name='дата добавление', auto_now_add=True)
    file = models.FileField(verbose_name='файл', upload_to='file/', blank=True)
    image = models.ImageField(verbose_name='изображения', upload_to='image/', blank=True)
    author = models.ForeignKey('Avtor', on_delete=models.PROTECT, verbose_name='автор', null=True,)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='категория')
    author_site = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', null=True)


    def __str__(self):
        return f'{self.title}'


class Works(models.Model):
    
    class Meta:
        verbose_name = 'автор-работа'
        verbose_name_plural = 'автор-работы'

    title = models.CharField(max_length=100, verbose_name='название книга')
    image = models.ImageField(verbose_name='изображения', upload_to='image/', blank=True)
    year = models.CharField(max_length=100, verbose_name='год издания')
    content =  models.TextField(verbose_name='контент')

    def __str__(self):
        return f'{self.title}'

class Avtor(models.Model):
    
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        
    title = models.CharField(max_length=100, verbose_name='имя автора')
    avtor = models.TextField(verbose_name='биография')
    img_Avtor = models.ImageField(verbose_name='изображения', upload_to='image/', blank=True)
    year_avtor = models.CharField(max_length=300, verbose_name='годы жизни', null=True)
    info = models.ManyToManyField('Works', verbose_name='книги автора')
    
    def __str__(self):
        return f'{self.title}'

class About(models.Model):

    class Meta:
        verbose_name = 'о нас'
        verbose_name_plural = 'о нас'

    title = models.CharField(max_length=300, verbose_name='заголовок')
    image = models.ImageField(verbose_name='изображение', upload_to='image/', null=True)
    content =  models.TextField(verbose_name='контент')


# Create your models here.