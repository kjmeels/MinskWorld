from django.db import models
from solo.models import SingletonModel


class AboutCompany(SingletonModel):
    """Модель 'О комании'."""

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    head_description = models.CharField(max_length=50, verbose_name="Верхнее описание")
    low_description = models.CharField(max_length=50, verbose_name="Нижнее описание")
    image = models.ImageField(
        upload_to="ac/ac/i", verbose_name="Изображение", blank=True, null=True
    )

    class Meta:
        verbose_name = verbose_name_plural = "О компании"

    def __str__(self):
        return self.title
