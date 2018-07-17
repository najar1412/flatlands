import os
from pathlib import Path

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import markdown

from .models import Article, Project


# TODO: IMP technical spec docs.
# TODO: IMP article/project images.

# IO
# TODO: refactor to markdown io to class
def read_markdown(md):
    """Opens markdown file and converts to str.
    md: io: markdown file to open.
    returns: str: markdown as str with html tags."""
    f = open(md, 'r')
    html = markdown.markdown(f.read())
    f.close()

    return html


def get_project_markdown(project=None, markdown=None):
    """Builds location information for accessing a markdown file.

    markdown: str: name of the markdown file.
    project: str: name of the project.
    return: str: markdown file convert to str, with html tags."""
    root = os.path.dirname(os.path.dirname(__file__))

    md = os.path.join(
        root, 'blog', 'static', 'blog', 'projects', project, 
        markdown, f'{markdown}.md'
    )

    return read_markdown(md)


def get_article_markdown(markdown=None):
    """Builds location information for accessing a markdown file.

    markdown: str: name of the markdown file.
    return: str: markdown file convert to str, with html tags."""
    root = os.path.dirname(os.path.dirname(__file__))

    md = os.path.join(
        root, 'blog', 'static', 'blog', 'articles', 
        markdown, f'{markdown}.md'
    )

    return read_markdown(md)


# DB
def get_project_nav(article_id, article_list):
    previous_id = None
    next_id = None

    for idx, article in enumerate(article_list):
        if article.pk == article_id:
            previous_id = idx - 1
            next_id = idx + 1

    if previous_id < 0:
        previous_id = -1
    else:
        previous_id = article_list[previous_id].pk

    if next_id > len(article_list) - 1:
        next_id = -1
    else:
        next_id = article_list[next_id].pk
    
    return (previous_id, next_id)


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
    post_markdown = get_article_markdown(markdown_name=post.content)

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
    viewed_article = [x for x in articles if x.pk == article_id][0]
    article_content = get_project_markdown(project=project.name, markdown=viewed_article.content)
    project_nav = get_project_nav(article_id, articles)

    context = {
        'project': project, 'articles': articles, 
        'viewed_article': viewed_article, 'article_content': article_content,
        'project_nav': project_nav
        }

    return render(request, 'blog/project_article.html', context)


def projects(request):
    projects = Project.objects.filter(published=True).order_by('-pub_date')
    context = {'projects': projects}

    return render(request, 'blog/projects.html', context)


def search(request):
    return render(request, 'blog/search.html')