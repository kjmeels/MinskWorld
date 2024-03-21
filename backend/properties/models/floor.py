from django.db import models


class Floor(models.Model):
    """Модель этажа."""

    entrance = models.ForeignKey(
        "properties.Entrance",
        on_delete=models.CASCADE,
        verbose_name="Подъезд",
        related_name="floors",
    )
    number = models.PositiveIntegerField(verbose_name="Номер")
    apartment_count = models.PositiveIntegerField(verbose_name="Количество квартир")

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"

    def __str__(self):
        return f"Этаж № - {self.number} в {self.entrance}"
