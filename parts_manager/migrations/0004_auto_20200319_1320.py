# Generated by Django 3.0.4 on 2020-03-19 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_manager', '0003_auto_20200319_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='code',
            field=models.CharField(max_length=20),
        ),
    ]
