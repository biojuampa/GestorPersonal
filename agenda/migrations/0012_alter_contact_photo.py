# Generated by Django 4.1.7 on 2023-02-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0011_rename_jobphone_phonejob_rename_position_job_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="agenda/contact/photo/nobody.png",
                null=True,
                upload_to="agenda/contact/photo/",
            ),
        ),
    ]