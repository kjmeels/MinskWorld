# Generated by Django 4.2.5 on 2024-03-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainPageTopSlide",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("head_text", models.CharField(max_length=30, verbose_name="Заглавный текст")),
                ("body_text", models.CharField(max_length=50, verbose_name="Второстепенный текст")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="mp/mpts/i", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Верхний слайд",
                "verbose_name_plural": "Верхние слайды",
            },
        ),
    ]
