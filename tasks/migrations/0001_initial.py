# Generated by Django 4.1.7 on 2023-02-27 22:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Priority",
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
                ("level", models.CharField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("headline", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("creation_date", models.DateField(default=django.utils.timezone.now)),
                ("deadline_date", models.DateField()),
                (
                    "priority",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.priority",
                    ),
                ),
            ],
        ),
    ]
