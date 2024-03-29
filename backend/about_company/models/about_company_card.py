from django.db import models


class AboutCompanyCard(models.Model):
    """Модель карточки 'О компании'."""

    head_title = models.CharField(max_length=50, verbose_name="Верхний заголовок")
    body_title = models.CharField(max_length=50, verbose_name="Нижний заголовок")

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    def __str__(self):
        return f"Карточка - {self.id}"
