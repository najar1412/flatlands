import os
from pathlib import Path

import markdown


class Markdown():
    def __init__(markdown, project=None):
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.markdown = markdown
        if project:
            self.article = os.path.join(
                self.root, 'blog', 'static', 'blog', 'projects', project, 
                self.markdown, f'{self.markdown}.md'
            )
        else:
            self.article = os.path.join(
                self.root, 'blog', 'static', 'blog', 'articles', 
                self.markdown, f'{self.markdown}.md'
            )


    def read_markdown(self, md):
        """Opens markdown file and converts to str.

        md: io: markdown file to open.
        returns: str: markdown as str with html tags."""
        f = open(md, 'r')
        html = markdown.markdown(f.read())
        f.close()

        return html


    def get(self):
        return self.read_markdown(self.article)


    def __repr__():
        return f'<Markdown({self.markdown}.md)>'