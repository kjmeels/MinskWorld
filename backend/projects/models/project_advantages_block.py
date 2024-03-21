from django.db import models
from solo.models import SingletonModel

from common.base_model import AbsOrder


class ProjectAdvantagesBlock(SingletonModel):
    title = models.CharField(verbose_name="Заголовок", max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = "Блок преимуществ"

    def __str__(self):
        return self._meta.verbose_name


class ProjectAdvantage(AbsOrder):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="project_advantages",
    )
    advantages_block = models.ForeignKey(
        "projects.ProjectAdvantagesBlock",
        on_delete=models.CASCADE,
        verbose_name="Блок преимуществ",
        related_name="project_advantages",
    )
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    image = models.ImageField(
        upload_to="p/pab/i", verbose_name="Изображение", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta(AbsOrder.Meta):
        verbose_name = "Преимущество проекта"
        verbose_name_plural = "Преимущества проекта"

    def __str__(self):
        return self.title
