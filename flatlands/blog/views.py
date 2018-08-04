from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article, Project, Tag
from .forms import SearchForm

from .modules.markdown import get_project_markdown, get_article_markdown
import blog.modules.helpers as helpers


# TODO: IMP project cover image

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
        'projects': projects,
        'searchform': SearchForm()
        }

    return render(request, 'blog/index.html', context)


def article(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    post_markdown = get_article_markdown(post.content)

    context = {
        'post': post, 
        'post_markdown': post_markdown,
        'searchform': SearchForm()
        }

    return render(request, 'blog/post.html', context)


def articles(request):
    articles = Article.objects.filter(project=None, published=True).order_by('-pub_date')

    context = {'articles': articles,
        'searchform': SearchForm()}

    return render(request, 'blog/articles.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = list(Article.objects.filter(project=project_id, published=True).order_by('pub_date'))

    context = {'project': project, 'articles': articles,
        'searchform': SearchForm()}

    if len(articles) > 0:
        return redirect('project_article', project_id=project_id, article_id=articles[0].pk)

    else:
        return render(request, 'blog/project.html', context)
    

def project_article(request, project_id, article_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = list(Article.objects.filter(project=project_id, published=True).order_by('pub_date'))
    viewed_article = [x for x in articles if x.pk == article_id][0]
    article_content = get_project_markdown(project.name, viewed_article.content)
    project_nav = get_project_nav(article_id, articles)

    context = {
        'project': project, 'articles': articles, 
        'viewed_article': viewed_article, 'article_content': article_content,
        'project_nav': project_nav,
        'searchform': SearchForm()
        }

    return render(request, 'blog/project_article.html', context)


def projects(request):
    projects = Project.objects.filter(published=True).order_by('-pub_date')

    context = {'projects': projects,
        'searchform': SearchForm()}

    return render(request, 'blog/projects.html', context)


def search(request, string):
    # TODO: something fishy going on. doesnt return all articles that include
    # the tag.
    cleaned_search = helpers.clean_string(string)
    articles = []

    for word in cleaned_search:
        for tag in Tag.objects.filter(name=word):
            article_query_set = tag.article_set.all()
            for article in article_query_set:
                articles.append(article)

    context = {
        'search': cleaned_search,
        'articles': set(articles),
        'searchform': SearchForm()
        }

    return render(request, 'blog/search.html', context)


def search_form(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search', string=form.cleaned_data['search'])

    return redirect('index')