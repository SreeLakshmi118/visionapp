import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('register', views.register, name='register'),
     path('logout', views.logout, name='logout'),
     path('book', views.book, name='book'),
     path('bookgen/<int:id1>', views.gencust, name='gencustomize'),
     path('booklang/<int:id2>', views.langcust, name='langcustomize'),
   
]

