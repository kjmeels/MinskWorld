from django.contrib.admin import register, ModelAdmin

from projects.models import Project


@register(Project)
class ProjectAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
