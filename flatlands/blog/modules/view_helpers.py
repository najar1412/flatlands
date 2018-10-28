"""
Contains additional functions for views.py
"""

def clean_string(string):
    # TODO: include removal os non-alphas
    # TODO: include whitespace colapsing
    """purges a string"""
    return ' '.join(string.split()).split(' ')


def before_and_after_articles(article_id, article_list):
    """
    projects contain multiple articles. this function will return the previous
    and next articles in the chain.
    AUG:
    article_id: ??: article id of currently viewed article.
    article_list: ??: ??
    """
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