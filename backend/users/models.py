from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import GenderChoices


class User(AbstractUser):
    full_name = models.CharField(max_length=50, verbose_name="Псевдоним")
    image = models.ImageField(
        upload_to="u/u/i", verbose_name="Фото пользователя", null=True, blank=True
    )
    age = models.PositiveIntegerField(verbose_name="Возраст", null=True, blank=True)
    gender = models.CharField(
        max_length=50, verbose_name="Пол", choices=GenderChoices.choices, default=GenderChoices.MALE
    )
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"
