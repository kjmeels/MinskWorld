from django.contrib.admin import register, ModelAdmin

from ..models import MortgageBank


@register(MortgageBank)
class MortgageBankAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
