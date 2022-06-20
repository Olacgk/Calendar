from django.contrib.gis.gdal.geometries import Point
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.v1.serializers.PlanningSerializer import PlanningSerializer
from event.models import Event
from planning.models import Planning


class EventSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Event
        geo_field = "coord"
        fields = ['id', 'activity', 'day_week', 'address', 'description', 'coord', 'planning', 'created', 'updated']
        read_only_fields = ['id', 'created', 'planning', 'updated']
