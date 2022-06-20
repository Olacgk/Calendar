from rest_framework import serializers

from planning.models import Planning


class PlanningSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = Planning
        fields = ['id', 'week_number', 'validated', 'created', 'updated', 'events']
        read_only_fields = ['id', 'created', 'updated']

    def get_events(self, obj):
        from api.v1.serializers.EventSerializer import EventSerializer
        return EventSerializer(obj.planning_events.all(), many=True).data

