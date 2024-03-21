from django.contrib.admin import register, ModelAdmin

from ..models import Building


@register(Building)
class BuildingAdmin(ModelAdmin):
    pass
