# Generated by Django 3.0.4 on 2020-03-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_manager', '0011_auto_20200324_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='備考'),
        ),
    ]
