from django.contrib import admin
from planning.models import Planning


# Register your models here.
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('week_number', 'validated', 'created', 'updated')


admin.site.register(Planning, PlanningAdmin)
