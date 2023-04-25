# Generated by Django 4.1.3 on 2022-12-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0005_rename_birth_contact_birthday"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="group_description",
            new_name="description",
        ),
        migrations.RemoveField(
            model_name="group",
            name="group_name",
        ),
        migrations.AddField(
            model_name="group",
            name="name",
            field=models.CharField(default="", max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="province",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="town",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="zipcode",
            name="zip_code",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]