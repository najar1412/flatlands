import os
from pathlib import Path

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import markdown

from .models import Article, Project


def get_markdown(article_name=None):
    root = os.path.dirname(os.path.dirname(__file__))
    articles = os.path.join(root, 'blog', 'static', 'blog', 'articles', article_name, f'{article_name}.md')

    f = open(articles, 'r')
    html = markdown.markdown(f.read())
    f.close()

    return html


def index(request):
    articles = Article.objects.filter(published=True, project=None).order_by('-pub_date')
    projects = Project.objects.filter(published=True).order_by('-pub_date')
    context = {
        'articles': articles,
        'projects': projects
        }

    return render(request, 'blog/index.html', context)


def article(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    post_markdown = get_markdown(post.content)
    context = {
        'post': post, 
        'post_markdown': post_markdown
        }

    return render(request, 'blog/post.html', context)


def articles(request):
    articles = Article.objects.filter(project=None, published=True).order_by('-pub_date')
    context = {'articles': articles}

    return render(request, 'blog/articles.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = list(Article.objects.filter(project=project_id, published=True).order_by('pub_date'))
    context = {'project': project, 'articles': articles}

    if len(articles) > 0:
        return redirect('project_article', project_id=project_id, article_id=articles[0].pk)

    else:
        return render(request, 'blog/project.html', context)
    

def project_article(request, project_id, article_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = list(Article.objects.filter(project=project_id, published=True).order_by('pub_date'))
    viewed_article = Article.objects.get(pk=article_id)
    article_content = post_markdown = get_markdown(viewed_article.content)
    context = {'project': project, 'articles': articles, 'viewed_article': viewed_article, 'article_content': article_content}

    return render(request, 'blog/project_article.html', context)


def projects(request):
    projects = Project.objects.filter(published=True).order_by('-pub_date')
    context = {'projects': projects}

    return render(request, 'blog/projects.html', context)


def search(request):
    return render(request, 'blog/search.html')