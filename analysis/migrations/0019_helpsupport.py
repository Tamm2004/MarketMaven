# Generated by Django 5.0.1 on 2024-03-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis", "0018_delete_form"),
    ]

    operations = [
        migrations.CreateModel(
            name="helpsupport",
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
                ("title", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
    ]
