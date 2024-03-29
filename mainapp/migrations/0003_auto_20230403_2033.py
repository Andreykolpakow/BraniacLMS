# Generated by Django 3.2.17 on 2023-04-03 20:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_data_migration"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="courseteachers",
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
            },
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={
                "ordering": ("course", "num"),
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ("-created",),
                "verbose_name": "News",
                "verbose_name_plural": "News",
            },
        ),
    ]
