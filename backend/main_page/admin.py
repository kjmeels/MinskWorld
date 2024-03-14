from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin import register, ModelAdmin

from main_page.models import MainPageTopSlide


@register(MainPageTopSlide)
class MainPageTopSlideAdmin(SortableAdminMixin, ModelAdmin):
    pass
