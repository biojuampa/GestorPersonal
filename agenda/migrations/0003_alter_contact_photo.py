# Generated by Django 4.1.3 on 2022-12-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0002_alter_company_location_alter_company_zip_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="photo",
            field=models.ImageField(
                blank=True, default="person/photo/nobody.png", upload_to="person/photo/"
            ),
        ),
    ]
