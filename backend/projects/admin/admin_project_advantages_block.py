from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib.admin import register, StackedInline
from solo.admin import SingletonModelAdmin

from ..models import ProjectAdvantagesBlock, ProjectAdvantage


class ProjectAdvantageInLine(SortableInlineAdminMixin, StackedInline):
    model = ProjectAdvantage
    extra = 0


@register(ProjectAdvantagesBlock)
class ProjectAdvantagesBlockAdmin(SortableAdminBase, SingletonModelAdmin):
    inlines = [ProjectAdvantageInLine]
