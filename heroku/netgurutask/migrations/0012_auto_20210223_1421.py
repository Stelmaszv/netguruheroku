# Generated by Django 3.0.8 on 2021-02-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netgurutask', '0011_car_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='avg_rating',
            field=models.FloatField(),
        ),
    ]
