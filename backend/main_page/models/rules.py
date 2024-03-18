from django.db import models
from solo.models import SingletonModel

from common.base_model import AbsOrder


class RulesBlock(SingletonModel):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="mp/rb/i", blank=True, null=True
    )

    class Meta:
        verbose_name = verbose_name_plural = "Блок правил"

    def __str__(self):
        return self._meta.verbose_name


class RulesSlide(AbsOrder):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    short_description = models.TextField(
        verbose_name="Короткое описание", max_length=150, blank=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    block = models.ForeignKey(
        "main_page.RulesBlock",
        on_delete=models.CASCADE,
        verbose_name="Блок правил",
        related_name="rules_slides",
    )

    class Meta(AbsOrder.Meta):
        verbose_name: str = "Слайд"
        verbose_name_plural: str = "Слайды"

    def __str__(self):
        return f"Слайд - {self.order}"
