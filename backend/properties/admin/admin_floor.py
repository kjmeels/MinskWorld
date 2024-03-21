from django.contrib.admin import register, ModelAdmin

from ..models import Floor


@register(Floor)
class FloorAdmin(ModelAdmin):
    pass
