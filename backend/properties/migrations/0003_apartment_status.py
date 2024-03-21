# Generated by Django 4.2.5 on 2024-03-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0002_apartment_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="status",
            field=models.CharField(
                choices=[("Sold", "Продана"), ("Free", "Свободна")],
                default="Free",
                max_length=50,
                verbose_name="Статус",
            ),
        ),
    ]
