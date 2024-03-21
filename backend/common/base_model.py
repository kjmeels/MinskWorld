from django.db import models


class AbsOrder(models.Model):
    """Базовый класс с сортировкой."""

    order = models.PositiveSmallIntegerField(verbose_name="Подряд", default=0)

    class Meta:
        abstract = True
        ordering = ("order",)
