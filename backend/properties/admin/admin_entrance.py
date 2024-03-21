from django.contrib.admin import register, ModelAdmin

from ..models import Entrance


@register(Entrance)
class EntranceAdmin(ModelAdmin):
    pass
