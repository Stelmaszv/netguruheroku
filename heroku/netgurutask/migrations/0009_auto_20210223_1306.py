# Generated by Django 3.0.8 on 2021-02-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netgurutask', '0008_auto_20210223_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
