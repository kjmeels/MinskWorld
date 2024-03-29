from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin import register, ModelAdmin

from ..models import AboutCompanyTeamSlide


@register(AboutCompanyTeamSlide)
class AboutCompanyTeamSlideAdmin(SortableAdminMixin, ModelAdmin):
    pass
