# Generated by Django 4.1.7 on 2023-03-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drinks', '0003_remove_drink_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='uid',
            field=models.CharField(default=12, max_length=8),
            preserve_default=False,
        ),
    ]
