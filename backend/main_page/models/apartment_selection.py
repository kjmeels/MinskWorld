from django.db import models

from ..constants import ApartmentSelectionCategoriesChoices


class ApartmentSelection(models.Model):
    category_name = models.CharField(
        verbose_name="Название катеогории",
        max_length=50,
        choices=ApartmentSelectionCategoriesChoices.choices,
        default=ApartmentSelectionCategoriesChoices.BUSINESS,
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="as/as/i", null=True, blank=True
    )

    class Meta:
        verbose_name: str = "Подборка квартир"
        verbose_name_plural: str = "Подборки квартир"

    def __str__(self):
        return f"Подборка квартир - {self.category_name}"
