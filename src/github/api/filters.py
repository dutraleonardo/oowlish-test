from rest_framework.filters import BaseFilterBackend
import coreapi


class QueryBaseFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
                coreapi.Field(
                    name='page',
                    location='query',
                    required=False,
                    type='int'
                ),
                coreapi.Field(
                    name='per_page',
                    location='query',
                    required=False,
                    type='int'
                ),
                coreapi.Field(
                    name='username',
                    location='query',
                    required=False,
                    type='string'
                ),
                coreapi.Field(
                    name='first',
                    location='query',
                    required=False,
                    type='boolean'
                ),
                coreapi.Field(
                    name='since',
                    location='query',
                    required=False,
                    type='int'
                ),
        ]
