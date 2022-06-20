from django.urls import path, include
from rest_framework import routers

from api.v1.viewsets.EventViewSet import EventViewSet
from api.v1.viewsets.PlanningViewSet import PlanningViewSet

router = routers.DefaultRouter()

router.register('plannings', PlanningViewSet, basename='plannings')
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
