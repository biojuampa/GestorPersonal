# Generated by Django 4.1.3 on 2022-12-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.location",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="zip_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.zipcode",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.country",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="province",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.province",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="town",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.town",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="zip_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agenda.zipcode",
            ),
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("names", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("nick_name", models.CharField(blank=True, max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.CharField(blank=True, max_length=100)),
                (
                    "photo",
                    models.ImageField(
                        default="person/photo/nobody.png", upload_to="person/photo/"
                    ),
                ),
                ("birthday", models.DateField(blank=True, null=True)),
                ("web", models.URLField(blank=True, max_length=100, null=True)),
                ("linked_in", models.URLField(blank=True, max_length=100, null=True)),
                ("twitter", models.CharField(blank=True, max_length=30, null=True)),
                ("facebook", models.URLField(blank=True, max_length=100, null=True)),
                ("instagram", models.CharField(blank=True, max_length=30, null=True)),
                ("whatsapp", models.PositiveIntegerField(blank=True, null=True)),
                ("note", models.TextField(blank=True, max_length=500, null=True)),
                ("groups", models.ManyToManyField(blank=True, to="agenda.group")),
                ("jobs", models.ManyToManyField(blank=True, to="agenda.job")),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agenda.location",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="phone",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.contact"
            ),
        ),
        migrations.DeleteModel(
            name="Person",
        ),
    ]
