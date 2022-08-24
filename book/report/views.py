from turtle import title
from email.mime import image
from django.conf import settings
from django.forms import FileField
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from report.models import *
from django.http import HttpResponse
from report.models import Book
from django.conf import os

booksImageSystem = FileSystemStorage('media/images/')
booksFileSystem = FileSystemStorage('media/file/')


def home(request): 
    report = Book.objects.all()[:5]
    return render(request, 'home.html', {'home': report})

def books(request):
    report = Book.objects.all()
    return render(request, 'book.html', {'books': report})

def avtors(request, id):
    report = Avtor.objects.filter(title=id)
    # report = Works.objects.filter(title=id)
    return render(request, 'author.html', {'avtors': report})

def authors(request):
    report = Avtor.objects.all()
    return render(request, 'authors.html', {'authors': report})

def aboute(request):
    report = About.objects.all()
    return render(request, 'about.html', {'aboute': report})

def category(request):
    book = Book.objects.all()
    categories = Categories.objects.all()
    return render(request, 'categories_b.html', {
        'book': book,
        'categories': categories
        })

def fiter_book(request, id):
    books = Book.objects.filter(category__id=id)
    return render(request, 'janry.html', {'books': books})

def item_books(request, id):
    books = Book.objects.get(id=id)
    categories = Categories.objects.all()
    return render(request, 'item_books.html', {'books': books, 'categories': categories})


def search_books(request):
    title = request.GET.get('search')
    authors = Avtor.objects.filter(title__icontains=title)
    books  = Book.objects.filter(title__icontains=title)
    return render(request, 'search.html',{
        'books': books, 
        'authors': authors,
        'categories': Categories.objects.all(), 
        'title': title
    })


def login_profile(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'auth/login.html', {})
    return redirect('/')


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def my_books(request):
    books = Book.objects.filter(author_site=request.user)
    categories = Categories.objects.all()
    return render(request, 'my_books/my_books.html', {'books': books, 'categories': categories})

def create_books(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        # author = request.POST.get('author')
        image = request.FILES['image']
        file = request.FILES['file']
        category = Categories.objects.get(id=request.POST.get('category'))
        author = Avtor.objects.get(id=request.POST.get('author'))
        print(author)
        desc = request.POST.get('description')   
        booksImageSystem.save(image.name, image)
        booksFileSystem.save(file.name, file)
        books = Book.objects.create(
            title = title,
            image = image,
            category = category,
            author = author,
            desc = desc,
            file = file,
            author_site=request.user
        )
        books.save()

        return redirect('/my_books/')
    author = Avtor.objects.all()
    categories = Categories.objects.all()
    return render(request, 'my_books/create_books.html', {'categories': categories, 'author': author,})
    
# def janry(request):
#     category = Categories.objects.all()
#     #news = News.objects.filter(category__slug=slug)
#     books = Book.objects.filter(category=category)
#     categories = Categories.objects.all()
#     return render(request, 'janry.html',{
#         'books': books, 
#         'categories': categories, 
#         'category': category,
#     })

# def download(request, path):
#     file_path=os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb')as fh:
#             response=HttpResponse(fh.read(),content_type="application/file")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response

#     raise 
# Create your views here.
