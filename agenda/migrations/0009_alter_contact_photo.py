# Generated by Django 4.1.3 on 2022-12-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0008_alter_company_options_alter_country_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="photo",
            field=models.ImageField(
                default="contact/photo/nobody.png", upload_to="contact/photo/"
            ),
        ),
    ]
