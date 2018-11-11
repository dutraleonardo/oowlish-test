from rest_framework import status
from rest_framework.response import Response

from ..utils import api_client as api


class ReadOnlyQueryApiGithubMixin(object):
    
    def get_queryset(self):
        filter = {}
        query_params_size = len(self.request.query_params)
        if query_params_size > 0:
            for field in self.request.query_params:
                param = self.request.query_params.get(field, None)
                if param:
                    filter[field] = param
                else:
                    pass
            return api.list_users(**filter)
        return api.list_users()