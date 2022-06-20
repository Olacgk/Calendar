import django.contrib.gis.db.models as geomodels
from django.db import models
from planning.models import Planning
# Create your models here.


class Event(models.Model):

    day_week = models.DateTimeField(auto_now=True)
    activity = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=255, blank=True, null=True)
    coord = geomodels.PointField(srid=4326)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time = models.TimeField(auto_now=True)
    planning = models.ForeignKey(Planning, related_name="planning_events", on_delete=models.CASCADE)

    # objects = geomodels.Manager()
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.activity)
