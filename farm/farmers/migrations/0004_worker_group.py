# Generated by Django 4.2 on 2024-12-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0003_mainprofile_supervisorprofile_workerprofile_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="worker",
            name="group",
            field=models.CharField(default="N/A", max_length=50),
        ),
    ]
