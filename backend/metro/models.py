from colorful.fields import RGBColorField
from django.db import models


class MetroLine(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50, unique=True)
    color = RGBColorField(verbose_name="Цвет")

    class Meta:
        verbose_name = "Ветка метро"
        verbose_name_plural = "Ветки метро"

    def __str__(self):
        return self.name


class MetroStation(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50, unique=True)
    line = models.ForeignKey(
        "metro.MetroLine",
        on_delete=models.CASCADE,
        verbose_name="Ветка метро",
        related_name="metro_stations",
    )

    class Meta:
        verbose_name = "Станция метро"
        verbose_name_plural = "Станции метро"
        ordering = ("line",)

    def __str__(self):
        return self.name
