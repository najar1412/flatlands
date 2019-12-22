from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:post_id>/', views.article, name='article'),
    path('search_form/', views.search_form, name='search_form'),
    path('search/<str:string>', views.search, name='search'),
    path('add_to_mailinglist/', views.add_to_mailinglist, name='add_to_mailinglist')
]