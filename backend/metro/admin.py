from django.contrib.admin import register, ModelAdmin

from .models import MetroLine, MetroStation


@register(MetroLine)
class MetroLineAdmin(ModelAdmin):
    pass


@register(MetroStation)
class MetroStationAdmin(ModelAdmin):
    pass
