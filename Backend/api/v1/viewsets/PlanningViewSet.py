from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.PlanningSerializer import PlanningSerializer
from planning.models import Planning


class PlanningPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PlanningViewSet(ModelViewSet):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
    pagination_class = PlanningPagination
