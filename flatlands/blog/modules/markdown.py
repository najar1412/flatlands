import os
from pathlib import Path

from bs4 import BeautifulSoup
import markdown


# TODO: refactor markdown functions to class.


def _static_loc(loc):
    """builds a folder location to be compatable with djangos static location
    loc: str: full location to file
    return: str: location usable by django"""

    path = os.path.normpath(loc)
    split_path = path.split(os.sep)

    for idx, folder in enumerate(split_path):
        if folder == 'static':

            return os.path.join(*split_path[idx: len(split_path)])


def _parse_html(loc, html):
    """parses str repr of html, looks for img tags and appends the correct
    static location
    loc: str: full location to file
    html: str: html to parse
    return: str"""

    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.findAll('img'):
        img['src'] = f"/{_static_loc(loc)}/{img['src']}"

    html = str(soup)

    return html


def _read_markdown(loc, md):
    """Opens markdown file and converts to str.
    md: io: markdown file to open.
    returns: str: markdown as str with html tags."""

    f = open(os.path.join(loc, md), 'r')
    html = markdown.markdown(f.read())
    f.close()

    return _parse_html(loc, html)


def get_project_markdown(project, markdown):
    """Builds location information for accessing a markdown file.

    markdown: str: name of the markdown file.
    project: str: name of the project.
    return: str: markdown file convert to str, with html tags."""

    root = os.path.dirname(os.path.dirname(__file__))

    loc = os.path.join(
        root, 'static', 'blog', 'projects', project, 
        markdown
    )

    md = f'{markdown}.md'

    return _read_markdown(loc, md)


def get_article_markdown(markdown):
    """Builds location information for accessing a markdown file.

    markdown: str: name of the markdown file.
    return: str: markdown file convert to str, with html tags."""

    root = os.path.dirname(os.path.dirname(__file__))

    loc = os.path.join(
        root, 'static', 'blog', 'articles', 
        markdown
    )
    md = f'{markdown}.md'

    return _read_markdown(loc, md)