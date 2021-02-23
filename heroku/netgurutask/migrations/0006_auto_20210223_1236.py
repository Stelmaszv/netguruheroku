# Generated by Django 3.0.8 on 2021-02-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netgurutask', '0005_car_rates_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='rates',
            field=models.ManyToManyField(to='netgurutask.Rate'),
        ),
    ]
