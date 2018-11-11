BASE_URL = 'https://api.github.com/'
USERS= 'users'
REPOS  = 'repos'
SEARCH = 'search'
USERS_SEARCH_URL = BASE_URL + SEARCH + '/' + USERS
REPO_URL = BASE_URL + USERS + '/{0}/' + REPOS
PAGINATION_URL = 'page={0}&per_page={1}'
USERS_URL = BASE_URL +  USERS