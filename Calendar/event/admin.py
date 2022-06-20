from django.contrib import admin
from event.models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('activity', 'description', 'day_week', 'planning', 'created')


admin.site.register(Event, EventAdmin)
