# Generated by Django 3.0.8 on 2021-02-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netgurutask', '0013_auto_20210223_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rates_number',
            field=models.IntegerField(),
        ),
    ]
