# Generated by Django 4.2.5 on 2024-03-19 11:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50, verbose_name="Название")),
                ("number", models.CharField(max_length=5, verbose_name="Номер здания")),
                ("address", models.CharField(max_length=50, verbose_name="Адрес")),
                (
                    "completion_year",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(2020),
                            django.core.validators.MaxValueValidator(2050),
                        ],
                        verbose_name="Год сдачи",
                    ),
                ),
                (
                    "completion_quarter",
                    models.CharField(
                        choices=[("I", "I"), ("II", "II"), ("III", "III"), ("IV", "IV")],
                        default="I",
                        max_length=50,
                        verbose_name="Квартал сдачи",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buildings",
                        to="projects.project",
                        verbose_name="Проект",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дом",
                "verbose_name_plural": "Дома",
            },
        ),
        migrations.CreateModel(
            name="Entrance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("number", models.PositiveSmallIntegerField(verbose_name="Номер подъезда")),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entrances",
                        to="properties.building",
                        verbose_name="Дом",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подъезд",
                "verbose_name_plural": "Подъезды",
            },
        ),
        migrations.CreateModel(
            name="Floor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("number", models.PositiveIntegerField(verbose_name="Номер")),
                ("apartment_count", models.PositiveIntegerField(verbose_name="Количество квартир")),
                (
                    "entrance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="floors",
                        to="properties.entrance",
                        verbose_name="Подъезд",
                    ),
                ),
            ],
            options={
                "verbose_name": "Этаж",
                "verbose_name_plural": "Этажи",
            },
        ),
        migrations.CreateModel(
            name="Apartment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("number", models.PositiveSmallIntegerField(verbose_name="Номер квартиры")),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=14, verbose_name="Стоимость"),
                ),
                (
                    "original_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=14, verbose_name="Начальная стоимость"
                    ),
                ),
                (
                    "price_per_meter",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена за квадратный метр"
                    ),
                ),
                (
                    "area",
                    models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Площадь"),
                ),
                ("class_name", models.CharField(max_length=50, verbose_name="Класс")),
                ("furnish", models.BooleanField(default=False, verbose_name="Отделка")),
                (
                    "room_count",
                    models.CharField(
                        choices=[
                            ("Studio", "Студия"),
                            ("One room", "1-а комн."),
                            ("Two room", "2-х комн."),
                            ("Three room", "3-х комн."),
                            ("Four room", "4-х комн."),
                            ("Five room", "5-ти комн."),
                            ("Six room", "6-ти комн."),
                        ],
                        default="Studio",
                        verbose_name="Количество комнат",
                    ),
                ),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="properties.building",
                        verbose_name="Дом",
                    ),
                ),
                (
                    "entrance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="properties.entrance",
                        verbose_name="Подъезд",
                    ),
                ),
                (
                    "floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="properties.floor",
                        verbose_name="Этаж",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="projects.project",
                        verbose_name="Проект",
                    ),
                ),
            ],
            options={
                "verbose_name": "Квартира",
                "verbose_name_plural": "Квартиры",
            },
        ),
        migrations.AddConstraint(
            model_name="apartment",
            constraint=models.UniqueConstraint(
                fields=("building", "number"), name="unique_building_number"
            ),
        ),
    ]
