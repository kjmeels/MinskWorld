from django.db import models
from common.base_model import AbsOrder


class AboutCompanyTeamSlide(AbsOrder):
    """Модель команды."""

    big_image = models.ImageField(
        upload_to="ac/act/bi", verbose_name="Большое изображение", blank=True, null=True
    )
    small_image = models.ImageField(
        upload_to="ac/act/si", verbose_name="Маленькое изображение", blank=True, null=True
    )
    background_image = models.ImageField(
        upload_to="ac/act/bi", verbose_name="Фоновое изображение", blank=True, null=True
    )
    year = models.PositiveSmallIntegerField(verbose_name="Год")
    full_name = models.CharField(verbose_name="Фамилия, Имя", max_length=30)
    description = models.CharField(max_length=50, verbose_name="Описание")

    class Meta(AbsOrder.Meta):
        verbose_name: str = "Слайд"
        verbose_name_plural: str = "Слайды"

    def __str__(self):
        return f"Слайд {self.id}"
