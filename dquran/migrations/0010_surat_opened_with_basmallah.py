# Generated by Django 4.1.5 on 2023-02-25 05:12
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("dquran", "0009_alter_ayatship_options_alter_surat_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="surat",
            name="opened_with_basmallah",
            field=models.BooleanField(default=True),
        ),
    ]
