from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.EventSerializer import EventSerializer
from event.models import Event


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

