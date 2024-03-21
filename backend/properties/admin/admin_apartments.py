from django.contrib.admin import register, ModelAdmin

from ..models import Apartment


@register(Apartment)
class ApartmentAdmin(ModelAdmin):
    readonly_fields = ("price_per_meter", "discount")
