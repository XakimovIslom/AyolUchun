# Generated by Django 4.2.7 on 2024-01-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_alter_course_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="tag",
            field=models.ManyToManyField(related_name="tags", to="course.tag"),
        ),
    ]
