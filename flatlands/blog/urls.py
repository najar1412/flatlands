from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:post_id>/', views.article, name='article'),
    path('projects/', views.projects, name='projects'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]