# Generated by Django 4.1 on 2023-04-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0008_remove_shows_theatre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="screen",
            name="no_of_total_seats",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
