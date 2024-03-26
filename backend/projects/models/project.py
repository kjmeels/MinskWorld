from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..constants import ProjectChoices


class Project(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=50, unique=True)
    slug = models.SlugField(verbose_name="Слаг", unique=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="p/p/i", null=True, blank=True)
    description = models.TextField(verbose_name="Примечание", null=True, blank=True)
    category = models.CharField(
        verbose_name="Категория",
        max_length=50,
        choices=ProjectChoices.choices,
        default=ProjectChoices.COMFORT,
    )
    metro_station = models.ForeignKey(
        "metro.MetroStation",
        on_delete=models.SET_NULL,
        verbose_name="Станция метро",
        related_name="projects",
        null=True,
    )
    time_to_station = models.PositiveSmallIntegerField(
        verbose_name="Время до метро",
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        null=True,
    )

    class Meta:
        verbose_name: str = "Проект"
        verbose_name_plural: str = "Проекты"

    def __str__(self):
        return f"Проект - {self.name}"
