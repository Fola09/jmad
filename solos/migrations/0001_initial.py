# Generated by Django 5.0.7 on 2024-07-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Solo",
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
                ("track", models.CharField(max_length=100)),
                ("artist", models.CharField(max_length=100)),
                ("instrument", models.CharField(max_length=50)),
            ],
        ),
    ]
