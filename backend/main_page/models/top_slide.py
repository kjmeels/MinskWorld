from django.db import models


class MainPageTopSlide(models.Model):
    """Верхние слайды главной страницы."""

    head_text = models.CharField(max_length=30, verbose_name="Заглавный текст")
    body_text = models.CharField(max_length=50, verbose_name="Второстепенный текст")
    image = models.ImageField(
        upload_to="mp/mpts/i", verbose_name="Изображение", blank=True, null=True
    )
    order = models.PositiveSmallIntegerField(verbose_name="порядок", default=0)

    class Meta:
        verbose_name: str = "Верхний слайд"
        verbose_name_plural: str = "Верхние слайды"
        ordering = ("order",)

    def __str__(self):
        return f"Слайд {self.id}"
