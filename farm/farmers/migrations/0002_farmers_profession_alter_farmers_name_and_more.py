# Generated by Django 5.1.2 on 2024-11-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmers",
            name="profession",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="farmers",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="farmers",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]
