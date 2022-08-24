"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
# from django.views.static import serve

from report.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('books/', books, name="books"),
    path('author/<str:id>', avtors, name="avtors"),
    path('authors/', authors, name="authors"),
    path('books_item/<int:id>/', item_books, name="item_books"),

    path('category/', category, name="category"),
    path('category/<int:id>/', fiter_book, name="fiter_book"),
    path('about-us/', aboute, name="aboute"),
    path('search/', search_books, name="search_books"),

    path('login/', login_profile, name='login'),
    path('logout/', logout_profile, name='logout'),

    path('my_books/', my_books, name='my_books'),
    path('my_books/create/', create_books, name='create_books'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

