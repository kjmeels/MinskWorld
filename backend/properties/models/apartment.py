from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from ..constants import RoomsCountChoices, StatusChoices


class Apartment(models.Model):
    """Модель квартиры."""

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="apartments",
        verbose_name="Проект",
    )
    building = models.ForeignKey(
        "properties.Building",
        on_delete=models.CASCADE,
        verbose_name="Дом",
        related_name="apartments",
    )
    entrance = models.ForeignKey(
        "properties.Entrance",
        on_delete=models.CASCADE,
        verbose_name="Подъезд",
        related_name="apartments",
    )
    floor = models.ForeignKey(
        "properties.Floor",
        on_delete=models.CASCADE,
        verbose_name="Этаж",
        related_name="apartments",
    )
    number = models.PositiveSmallIntegerField(verbose_name="Номер квартиры")
    price = models.DecimalField(decimal_places=2, max_digits=14, verbose_name="Стоимость")
    original_price = models.DecimalField(
        decimal_places=2, max_digits=14, verbose_name="Начальная стоимость"
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name="Скидка", default=0, validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    price_per_meter = models.DecimalField(
        decimal_places=2, max_digits=10, verbose_name="Цена за квадратный метр"
    )
    area = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Площадь")
    class_name = models.CharField(verbose_name="Класс", max_length=50)
    furnish = models.BooleanField(verbose_name="Отделка", default=False)
    room_count = models.CharField(
        verbose_name="Количество комнат",
        choices=RoomsCountChoices.choices,
        default=RoomsCountChoices.STUDIO,
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.FREE,
    )

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        constraints = [
            UniqueConstraint(fields=["building", "number"], name="unique_building_number")
        ]

    def save(self, *args, **kwargs):
        if self.price and self.area:
            self.price_per_meter = self.price / self.area
        if self.price and self.original_price:
            self.discount = (self.original_price - self.price) / self.original_price * 100
        super().save()

    def __str__(self):
        return f"Квартира № {self.number}"
