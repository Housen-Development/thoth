# Generated by Django 3.0.4 on 2020-03-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_manager', '0009_auto_20200324_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='remarks',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='備考'),
        ),
    ]
