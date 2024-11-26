# Generated by Django 5.1.2 on 2024-11-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0003_tasks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workers",
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
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("workertype", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AlterField(
            model_name="tasks",
            name="role",
            field=models.CharField(max_length=100),
        ),
    ]
