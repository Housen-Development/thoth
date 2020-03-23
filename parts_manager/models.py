import datetime

from django.db import models
from django.utils import timezone


class Parts(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    remarks = models.CharField('備考', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PartsInOut(models.Model):
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    warehousing = models.IntegerField('入庫数', default=0)
    shipping = models.IntegerField('出庫数', default=0)
    input_date = models.DateTimeField('入力日', auto_now_add=True)

    class Meta:
        ordering = ['parts__code']

    def __str__(self):
        return f'{self.location.name} - {self.parts.name}'

    def is_input_date_future(self):
        """ input_dateが現在の時間より未来の場合 :return: True """
        return self.input_date > timezone.now()
