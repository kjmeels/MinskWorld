from collections import defaultdict

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

from ..constants import MortgageChoices
from ..querysets import MortgageQuerySet


class MortgageOffer(models.Model):
    bank = models.ForeignKey(
        "mortgage.MortgageBank",
        on_delete=models.CASCADE,
        verbose_name="Предложение банка",
        related_name="mortgage_offers",
    )
    min_sum = models.PositiveIntegerField(verbose_name="Минимальная сумма кредита")
    max_sum = models.PositiveIntegerField(verbose_name="Максимальная сумма кредита")
    min_term = models.PositiveIntegerField(
        verbose_name="Минимальный срок", validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    max_term = models.PositiveIntegerField(
        verbose_name="Максимальный срок", validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    rate = models.PositiveSmallIntegerField(verbose_name="Ставка", default=0)
    type = models.CharField(
        verbose_name="Тип",
        max_length=50,
        choices=MortgageChoices.choices,
        default=MortgageChoices.STANDART,
    )
    objects = MortgageQuerySet.as_manager()

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def clean(self, *args, **kwargs):
        super().clean()
        errors = defaultdict(list)
        if self.min_sum >= self.max_sum:
            errors["min_sum"].append(
                f"Минимальная сумма не может быть больше или равной максимальной суммы"
            )
        if self.min_term >= self.max_term:
            errors["min_term"].append(
                f"Минимальный срок не может быть юольше или равным максимальному сроку"
            )
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"Банк - {self.bank}, id - {self.pk}"
