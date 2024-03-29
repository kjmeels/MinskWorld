from django.contrib.admin import register, ModelAdmin

from ..models import AboutCompanyCard


@register(AboutCompanyCard)
class AboutCompanyCardAdmin(ModelAdmin):
    pass
