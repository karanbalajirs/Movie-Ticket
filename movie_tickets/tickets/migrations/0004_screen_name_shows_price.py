# Generated by Django 4.1 on 2023-04-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0003_alter_movies_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="screen",
            name="name",
            field=models.CharField(default="main", max_length=50),
        ),
        migrations.AddField(
            model_name="shows", name="price", field=models.IntegerField(default=150),
        ),
    ]
