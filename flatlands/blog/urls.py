from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.blog_post, name='blog_post'),
    path('code/', views.code, name='code'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]