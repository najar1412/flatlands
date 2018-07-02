from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Article, Project


def index(request):
    articles = Article.objects.order_by('-pub_date')

    context = {
        'articles': articles
        }

    return render(request, 'blog/index.html', context)


def article(request, post_id):
    post = get_object_or_404(Article, pk=post_id)

    return render(request, 'blog/post.html', {'post': post})


def articles(request):
    articles = Article.objects.order_by('-pub_date')

    context = {'articles': articles}

    return render(request, 'blog/articles.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = list(Article.objects.filter(project=project_id).order_by('pub_date'))

    context = {'project': project, 'articles': articles}

    return render(request, 'blog/project.html', context)


def projects(request):
    projects = Project.objects.order_by('-pub_date')
    
    context = {'projects': projects}

    return render(request, 'blog/projects.html', context)


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    return render(request, 'blog/search.html')