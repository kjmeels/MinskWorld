# Generated by Django 4.2.5 on 2024-03-19 11:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0004_rulesblock_rulesslide"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rulesslide",
            options={
                "ordering": ("order",),
                "verbose_name": "Слайд",
                "verbose_name_plural": "Слайды",
            },
        ),
    ]