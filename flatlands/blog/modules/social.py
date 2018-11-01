"""
Source code for social platform interactions
"""

# TODO: cache data to database
# TODO: move cred to config.py

import requests

from blog.models import SocialInstagram
import blog.config


# insta_token = "498923891.1677ed0.c322b044058840b490d5e0386a0aa421"

def _cache_instagram_links_to_db():
    """caching function: accesses instagram api for latest posts, and caches to database"""
    links = []
    payload = {'access_token': blog.config.Config().INSTAGRAM_TOKEN}
    res = requests.get('https://api.instagram.com/v1/users/self/media/recent/', params=payload).json()

    if 'data' in res and res['data']:
        for post in res['data']:
            links.append(post['link'])

    for link in links[:4]:
        payload = {
            'url': link,
            'hidecaption': True
            }

        res = requests.get('https://api.instagram.com/oembed', params=payload).json()

        new_post = SocialInstagram(link=link, oembed=res['html'])
        new_post.save()


def get_latest_instagram():
    """quries database for all instagram posts"""
    # TODO: convert to json
    return SocialInstagram.objects.all()[:3]