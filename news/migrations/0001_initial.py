# Generated by Django 5.1 on 2024-08-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=80, verbose_name="Название")),
                (
                    "preview",
                    models.CharField(blank=True, max_length=200, verbose_name="Анонс"),
                ),
                ("text", models.TextField(verbose_name="Содержание")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
                ("source", models.CharField(max_length=50, verbose_name="Источник")),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]