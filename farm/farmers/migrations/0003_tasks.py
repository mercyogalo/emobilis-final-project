# Generated by Django 5.1.2 on 2024-11-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0002_farmers_profession_alter_farmers_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tasks",
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
                ("name", models.CharField(max_length=100)),
                ("role", models.EmailField(max_length=254)),
                ("heading", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("days", models.IntegerField()),
            ],
        ),
    ]