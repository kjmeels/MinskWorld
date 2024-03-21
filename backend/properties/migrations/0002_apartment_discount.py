# Generated by Django 4.2.5 on 2024-03-19 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="discount",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(99),
                ],
                verbose_name="Скидка",
            ),
        ),
    ]