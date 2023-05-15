import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('register', views.register, name='register'),
     path('main', views.main, name='main'),
     path('about', views.about, name='about'),
     path('logout', views.logout, name='logout'),
     path('book', views.book, name='book'),
     path('bookgen/<int:id1>', views.gencust, name='gencustomize'),
     path('booklang/<int:id2>', views.langcust, name='langcustomize'),
     path('quiz', views.quiz_view, name='quiz'),
     path('quiz_results/', views.quiz_results, name='quiz_results'),
     path('quizview', views.quizview, name='quizview'),
     path('search/<str:lang>/<str:gen>/', views.search, name='search'),
     
   
]

