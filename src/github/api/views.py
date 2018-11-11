from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from ..utils import api_client as api
from .mixins import ReadOnlyQueryApiGithubMixin
from .filters import QueryBaseFilterBackend


class GithubUsersApiViewSet(ReadOnlyQueryApiGithubMixin, GenericViewSet):
    filter_backends = (QueryBaseFilterBackend, )

    def list(self, request):
        query = self.get_queryset()
        return Response(query)
        
    @action(methods=['get'], detail=True)
    def repos(self, request, username=None):
        return Response(api.get_repos_by_user(username))
