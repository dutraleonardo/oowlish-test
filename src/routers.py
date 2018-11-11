from rest_framework.routers import SimpleRouter, DefaultRouter
from github.api.views import GithubUsersApiViewSet

router_v1 = SimpleRouter(trailing_slash=False)
router_v1.register('github_users', GithubUsersApiViewSet, base_name='github_api')