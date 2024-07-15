# Generated by Django 5.0.6 on 2024-07-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boaapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioFile",
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
                ("file", models.FileField(upload_to="audio/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]