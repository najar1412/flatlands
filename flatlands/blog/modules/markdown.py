"""
Source code for handling all markdown logic
"""

import os
from pathlib import Path

from bs4 import BeautifulSoup
import markdown


# Assumes the following structure
# /markdown_root
#   /markdown_type(can nest)
#       /markdown_name_folder
#           /['markdown_file', 'assets']

class MarkdownStore():
    """
    builds MTML safe strings for locations to markdown files

    AUG:
    component: str: name of component to use to find markdown 
    and assiated files.

    EXTENSTION:
    additinal compounents can be added by appending its name to 
    self._COMPONENTS and adding a function with the same name 
    prefixed with '_'.
    'new_component': _new_component()
    """
    # TODO: rename set, to something not python reserved :p
    def __init__(self, component):
        self._COMPONENTS = {
            'django': self._django(), 
            #'new_component': '_new_component()'
        }

        if component in self._COMPONENTS:
            self.component = component
            self.endpoint = self._COMPONENTS[component]


    def _django(self):
        """EXAMPLE: component that links to djangos static folder"""
        # TODO: need to implement a way for the user to 
        # define the django app name to remove 'blog' hardcode.
        # or i can retrieve the app name from the root?
        root = os.path.dirname(os.path.dirname(__file__))
        loc = os.path.join(
            root, 'static', 'blog'
        )

        return loc


    def set(self):
        return self.endpoint


    def __repr__(self):
        return f'<MarkdownStore(component={self.component})>'


class MTML():
    """handles retrival and conversion of markdown files to html"""
    # TODO: remove hardcodings to locations, try and imp 
    # MarkdownStore where poss.
    def __init__(self, static=None):
        if static:
            self.static = MarkdownStore(static).set()
        else:
            self.static = MarkdownStore('django').set()

        self.markdown_type = None


    def _wrap(self, to_wrap, wrap_in):
        """utility to wrap one tag with another
        AUG:
        to_wrap: BS4 tag element.
        wrap_in: BS4 constructed tag"""
        contents = to_wrap.replace_with(wrap_in)
        wrap_in.append(contents)


    def _parse_headers(self, markdown_contents):
        """get all headers from a markdown file"""
        # TODO: this shouldnt be called seprately,
        # instead it should be built when a markdown file is retrieved.
        html = BeautifulSoup(markdown_contents, 'html.parser')
        results = [x.get_text() for x in html.findAll('h3')]

        return results


    def _parse_markdown_contents(self, markdown_contents):
        """parse markdown contents to html
        loc: str: full location to file
        markdown_contents: str: markdown_contents to parse
        return: str
        """
        # TODO: remove hardcodings, blog etc
        # better string builder for parsing img tags
        html = BeautifulSoup(markdown_contents, 'html.parser')

        # update img tags
        for img in html.findAll('img'):
            markdown_location = '/'.join(self.markdown_type)
            img['src'] = f"/static/blog/{markdown_location}/{self.md}/{img['src']}"

        # update h3 tags
        for h3 in html.findAll('h3'):
            new_tag = html.new_tag("a")
            new_tag['id'] = h3.get_text()

            self._wrap(h3, new_tag)

        return str(html)

    
    def _convert_markdown(self, loc):
        """Opens markdown file in memory.
        returns: str: markdown as html.
        """
        with open(os.path.join(loc, f'{self.md}.md'), 'r') as f:
            return self._parse_markdown_contents(markdown.markdown(f.read(), extensions=['markdown.extensions.tables', 'tables']))


    def retrieve(self, markdown, markdown_type=None):
        """retrieves a markdown file as html.
        markdown: str: name of the markdown file.
        markdown_type: str: folder name for the type of markdown file. 
            For example 'article', 'post' or 'document'
        return: str: markdown file converted to html.
        """
        self.markdown_type = markdown_type
        self.md = markdown
        loc = os.path.join(self.static, *markdown_type, markdown)
        md_contents = self._convert_markdown(loc)

        return md_contents


    def __repr__(self):
        return f'<MTML(static={self.static})>'