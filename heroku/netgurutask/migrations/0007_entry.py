# Generated by Django 3.0.8 on 2021-02-23 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netgurutask', '0006_auto_20210223_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netgurutask.Car')),
                ('rates', models.ManyToManyField(to='netgurutask.Rate')),
            ],
        ),
    ]
