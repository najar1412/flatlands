from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:post_id>/', views.article, name='article'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('projects/<int:project_id>/<int:article_id>/', views.project_article, name='project_article'),
    path('articles/', views.articles, name='articles'),
    path('search_form/', views.search_form, name='search_form'),
    path('search/<str:string>', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('add_to_mailinglist/', views.add_to_mailinglist, name='add_to_mailinglist')
]