# Generated by Django 3.0.4 on 2020-03-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_manager', '0012_auto_20200324_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='partsinout',
            name='input_date',
            field=models.DateTimeField(auto_now=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='partsinout',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新日'),
        ),
    ]
