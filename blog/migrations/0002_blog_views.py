# Generated by Django 4.2.7 on 2024-01-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="views",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]