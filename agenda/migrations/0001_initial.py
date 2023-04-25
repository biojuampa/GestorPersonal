# Generated by Django 4.1.3 on 2022-12-04 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(blank=True, max_length=500)),
                ("address", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=30)),
                (
                    "flag",
                    models.ImageField(
                        blank=True, null=True, upload_to="flags/countries/"
                    ),
                ),
                (
                    "coat",
                    models.ImageField(
                        blank=True, null=True, upload_to="coats/countries/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group",
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
                ("group_name", models.CharField(max_length=15)),
                ("group_description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("position", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, max_length=500)),
                ("address", models.CharField(blank=True, max_length=100)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="agenda.company"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="agenda.country"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("birthday", models.DateField()),
                ("web", models.URLField(blank=True, max_length=100, null=True)),
                ("linked_in", models.URLField(blank=True, max_length=100, null=True)),
                ("twitter", models.CharField(blank=True, max_length=30, null=True)),
                ("facebook", models.URLField(blank=True, max_length=100, null=True)),
                ("instagram", models.CharField(blank=True, max_length=30, null=True)),
                ("whatsapp", models.PositiveIntegerField(blank=True, null=True)),
                ("note", models.TextField(max_length=500)),
                ("groups", models.ManyToManyField(to="agenda.group")),
                ("jobs", models.ManyToManyField(to="agenda.job")),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agenda.location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Province",
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
                ("name", models.CharField(max_length=30)),
                (
                    "flag",
                    models.ImageField(
                        blank=True, null=True, upload_to="flags/provinces/"
                    ),
                ),
                (
                    "coat",
                    models.ImageField(
                        blank=True, null=True, upload_to="coats/provinces/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Town",
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
                ("name", models.CharField(max_length=30)),
                (
                    "flag",
                    models.ImageField(blank=True, null=True, upload_to="flags/towns/"),
                ),
                (
                    "coat",
                    models.ImageField(blank=True, null=True, upload_to="coats/towns/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ZipCode",
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
                ("zip_code", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
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
                ("number", models.PositiveIntegerField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="agenda.person"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="location",
            name="province",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.province"
            ),
        ),
        migrations.AddField(
            model_name="location",
            name="town",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.town"
            ),
        ),
        migrations.AddField(
            model_name="location",
            name="zip_code",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.zipcode"
            ),
        ),
        migrations.CreateModel(
            name="JobPhone",
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
                ("number", models.PositiveIntegerField()),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="agenda.job"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.location"
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="zip_code",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agenda.zipcode"
            ),
        ),
    ]