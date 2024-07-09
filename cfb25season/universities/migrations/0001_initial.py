# Generated by Django 5.0.6 on 2024-07-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="University",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("logo_url", models.URLField()),
                ("schedule", models.JSONField(default=dict)),
                ("recent_game", models.JSONField(default=dict)),
                ("stats", models.JSONField(default=dict)),
            ],
        ),
    ]
