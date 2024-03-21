from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..constants import QuartersChoices
from ..querysets import BuildingQuerySet


class Building(models.Model):
    """Модель дома."""

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="buildings",
    )
    name = models.CharField(verbose_name="Название", max_length=50, blank=True)
    number = models.CharField(verbose_name="Номер здания", max_length=5)
    address = models.CharField(verbose_name="Адрес", max_length=50)
    completion_year = models.PositiveSmallIntegerField(
        verbose_name="Год сдачи", validators=[MinValueValidator(2020), MaxValueValidator(2050)]
    )
    completion_quarter = models.CharField(
        verbose_name="Квартал сдачи",
        max_length=50,
        choices=QuartersChoices.choices,
        default=QuartersChoices.FIRST_QUARTER,
    )

    objects = BuildingQuerySet.as_manager()

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"

    def __str__(self):
        return self.name
