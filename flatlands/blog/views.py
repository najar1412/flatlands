from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post, Project, Tag, Mailing_List
from .forms import SearchForm, MailingList

from .modules.markdown import MTML
import blog.modules.view_helpers as view_helpers
from .modules.social import get_latest_instagram, _cache_instagram_links_to_db
from .models import UsedSoftware


# TODO: imp embedded socials
# TODO: imp 'posts in series' for articles

# NEEDED FOR ALL REQUESTS, IMP DECORATOR
standard_context = {
    'instagram_content': get_latest_instagram(),
    'searchform': SearchForm(),
    'mailing_list_form': MailingList()
    }


def add_to_mailinglist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailingList(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']

            new_email = Mailing_List(email=email)
            new_email.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        return redirect('index')

# views
def index(request):
    """Landing page"""
    # TODO: cache needs to happen somewhere else.
    # CACHE instagram
    # _cache_instagram_links_to_db()

    articles = Post.objects.filter(
        published=True, project=None
        ).order_by('-pub_date')

    projects = Project.objects.filter(
        published=True
        ).order_by('-pub_date')

    context = standard_context
    context['articles'] = articles
    context['projects'] = projects


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

    context = standard_context
    context['post'] = post
    context['post_markdown'] = post_markdown
    context['markdown_headers'] = markdown_headers


    return render(request, 'blog/post.html', context)


def articles(request):
    """retrives all articles"""
    articles = Post.objects.filter(
        project=None, published=True
        ).order_by('-pub_date')

    context = standard_context
    context['articles'] = articles


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

    context = standard_context
    context['project'] = project
    context['articles'] = articles


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

        markdown_headers = MTML('django')._parse_headers(project_markdown)

        project_nav = view_helpers.before_and_after_articles(
            article_id, articles
            )

        used_software = UsedSoftware.objects.filter(projects=project_id)

        context = standard_context
        context['project'] = project
        context['used_software'] = used_software
        context['articles'] = articles
        context['viewed_article'] = article
        context['article_content'] = project_markdown
        context['project_nav'] = project_nav
        context['markdown_headers'] = markdown_headers


        return render(request, 'blog/project_article.html', context)

    return redirect('index')


def projects(request):
    """retrives all projects"""
    projects = Project.objects.filter(
        published=True
        ).order_by('-pub_date')

    context = standard_context
    context['projects'] = projects

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

    context = standard_context
    context['search'] = cleaned_search
    context['articles'] = set(articles)


    return render(request, 'blog/search.html', context)


def search_form(request):
    """Parses/cleans search field data"""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search', string=form.cleaned_data['search'])

    return redirect('index')