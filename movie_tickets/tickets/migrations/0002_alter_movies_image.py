# Generated by Django 4.1 on 2023-04-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="image",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
    ]