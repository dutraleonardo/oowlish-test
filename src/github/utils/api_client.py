from requests import get

from rest_framework import status
from .api_urls import USERS_SEARCH_URL, REPO_URL, PAGINATION_URL, USERS_URL

DEFAULT_PER_PAGE = 50 


def get_url_query(page=1, per_page=None, first=None, since=None, username=None):
    first = True if first == 'true' else False
    per_page = per_page if per_page is not None else DEFAULT_PER_PAGE
    per_page = 1 if first is True else per_page
    pagination = PAGINATION_URL
    since = '' if (since is None and username is None) else 'since={0}'.format(since)
    query = USERS_SEARCH_URL + '?q={0}+in:login'.format(username) if username is not None else USERS_URL
    query = query + '?' + pagination.format(page, per_page) \
        if USERS_URL in query else query + '&' + pagination.format(page, per_page)
    pagination.format(page, per_page)
    query = query + '&' + since if since is not None else query
    return query


def list_users(**kwargs):
    url_query = get_url_query(**kwargs)
    print(url_query)
    response = get(url_query).json()
    return response


def get_repos_by_user(username):
    repo_usarname_url = REPO_URL
    response = get(repo_usarname_url.format(username))
    print(response.json())
    return response.json() if response.status_code == 200 else status.HTTP_404_NOT_FOUND
