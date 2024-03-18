from django.contrib.admin import register, ModelAdmin

from ..models import ApartmentSelection


@register(ApartmentSelection)
class ApartmentSelectionAdmin(ModelAdmin):
    pass
