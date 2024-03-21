from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib.admin import register, StackedInline
from solo.admin import SingletonModelAdmin

from ..models import RulesSlide, RulesBlock


class RulesSlideInline(SortableInlineAdminMixin, StackedInline):
    model = RulesSlide
    extra = 0


@register(RulesBlock)
class RulesBlockAdmin(SortableAdminBase, SingletonModelAdmin):
    inlines = [RulesSlideInline]
