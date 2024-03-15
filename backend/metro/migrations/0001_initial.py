# Generated by Django 4.2.5 on 2024-03-14 11:54

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MetroLine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Название")),
                ("color", colorful.fields.RGBColorField(verbose_name="Цвет")),
            ],
            options={
                "verbose_name": "Ветка метро",
                "verbose_name_plural": "Ветки метро",
            },
        ),
        migrations.CreateModel(
            name="MetroStation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Название")),
                (
                    "line",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metrostations",
                        to="metro.metroline",
                        verbose_name="Ветка метро",
                    ),
                ),
            ],
            options={
                "verbose_name": "Станция метро",
                "verbose_name_plural": "Станции метро",
                "ordering": ("line",),
            },
        ),
    ]
