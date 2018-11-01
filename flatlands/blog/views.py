from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post, Project, Tag
from .forms import SearchForm

from .modules.markdown import MTML
import blog.modules.view_helpers as view_helpers


# TODO: imp post linking
# TODO: imp embedded socials
# TODO: imp 'posts in series' for articles

# views
def index(request):
    """Landing page"""
    articles = Post.objects.filter(
        published=True, project=None
        ).order_by('-pub_date')

    projects = Project.objects.filter(
        published=True
        ).order_by('-pub_date')

    context = {
        'articles': articles,
        'projects': projects,
        'searchform': SearchForm()
        }

    return render(request, 'blog/index.html', context)


def about(request):
    # TODO: IMP design and copy
    return render(request, 'blog/about.html')


def article(request, post_id):
    """retrives a single articles"""
    post = get_object_or_404(Post, pk=post_id)
    post.viewed += 1
    post.save()

    post_markdown = MTML('django').retrieve(
        post.content, markdown_type=['articles']
        )

    markdown_headers = MTML('django')._parse_headers(post_markdown)

    context = {
        'post': post, 
        'post_markdown': post_markdown,
        'searchform': SearchForm(),
        'markdown_headers': markdown_headers
        }

    return render(request, 'blog/post.html', context)


def articles(request):
    """retrives all articles"""
    articles = Post.objects.filter(
        project=None, published=True
        ).order_by('-pub_date')

    context = {
        'articles': articles,
        'searchform': SearchForm()
        }

    return render(request, 'blog/articles.html', context)


def project(request, project_id):
    """retrives a single project"""
    project = get_object_or_404(Project, pk=project_id)
    articles = list(
        Post.objects.filter(
            project=project_id, published=True
            ).order_by('pub_date')
        )

    context = {'project': project, 'articles': articles,
        'searchform': SearchForm()}

    if len(articles) > 0:
        return redirect(
            'project_article', project_id=project_id, article_id=articles[0].pk
            )

    else:
        return render(request, 'blog/project.html', context)
    

def project_article(request, project_id, article_id):
    """retrives a single projects article
    AUG:
    project_id: ??: pk of a project
    article_id: ??: pk of an article
    """
    # TODO: Limit data return to minimum. 
    # why send the whole project row, if i just need the title etc.
    article = get_object_or_404(Post, pk=article_id)

    if article:
        project = get_object_or_404(Project, pk=project_id)
        articles = list(
            Post.objects.filter(
                project=project_id, published=True
                ).order_by('pub_date')
            )

        project_markdown = MTML('django').retrieve(
            article.content, markdown_type=['projects', project.name]
            )

        project_nav = view_helpers.before_and_after_articles(
            article_id, articles
            )

        context = {
            'project': project, 
            'articles': articles, 
            'viewed_article': article, 
            'article_content': project_markdown,
            'project_nav': project_nav,
            'searchform': SearchForm()
            }

        return render(request, 'blog/project_article.html', context)

    return redirect('index')


def projects(request):
    """retrives all projects"""
    projects = Project.objects.filter(
        published=True
        ).order_by('-pub_date')

    context = {
        'projects': projects,
        'searchform': SearchForm()
        }

    return render(request, 'blog/projects.html', context)


def search(request, string):
    """retrives tags for article retrieval
    AUG:
    string: str??: keywords sepr by single spaces
    """
    # TODO: something fishy going on. doesnt return all articles that include
    # the tag.
    cleaned_search = view_helpers.clean_string(string)
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
    """Parses/cleans search field data"""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search', string=form.cleaned_data['search'])

    return redirect('index')