from django.db import models


class MortgageBank(models.Model):
    name = models.CharField(verbose_name="Название банка", max_length=50, unique=True)
    slug = models.SlugField(verbose_name="Слаг", unique=True)
    logo = models.ImageField(verbose_name="Логотип", upload_to="m/mb/l", null=True, blank=True)

    class Meta:
        verbose_name = "Банк"
        verbose_name_plural = "Банки"

    def __str__(self):
        return self.name
