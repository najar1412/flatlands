from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Article


def index(request):
    blog_posts = Article.objects.order_by('-pub_date')
    context = {'blog_posts': blog_posts}

    return render(request, 'blog/index.html', context)


def article(request, post_id):
    post = get_object_or_404(Article, pk=post_id)

    return render(request, 'blog/post.html', {'post': post})


def articles(request):
    blog_posts = Article.objects.order_by('-pub_date')
    context = {'blog_posts': blog_posts}

    return render(request, 'blog/articles.html', context)


def projects(request):
    return render(request, 'blog/projects.html')


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    return render(request, 'blog/search.html')