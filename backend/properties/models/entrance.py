from django.db import models


class Entrance(models.Model):
    """Модель подъезда."""

    building = models.ForeignKey(
        "properties.Building",
        on_delete=models.CASCADE,
        verbose_name="Дом",
        related_name="entrances",
    )
    number = models.PositiveSmallIntegerField(verbose_name="Номер подъезда")

    class Meta:
        verbose_name = "Подъезд"
        verbose_name_plural = "Подъезды"

    def __str__(self):
        return f"Подъезд №{self.number} - {self.building.name}"
