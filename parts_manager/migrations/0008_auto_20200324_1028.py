# Generated by Django 3.0.4 on 2020-03-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_manager', '0007_auto_20200323_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsinout',
            name='shipping',
            field=models.PositiveIntegerField(default=0, verbose_name='出庫数'),
        ),
        migrations.AlterField(
            model_name='partsinout',
            name='warehousing',
            field=models.PositiveIntegerField(default=0, verbose_name='入庫数'),
        ),
    ]
