# Generated by Django 4.2.5 on 2024-03-15 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("metro", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metrostation",
            name="line",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="metro_stations",
                to="metro.metroline",
                verbose_name="Ветка метро",
            ),
        ),
    ]