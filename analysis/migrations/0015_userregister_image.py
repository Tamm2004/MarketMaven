# Generated by Django 5.0.1 on 2024-02-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis", "0014_userregister_address_userregister_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userregister",
            name="image",
            field=models.ImageField(blank=True, upload_to="media"),
        ),
    ]
