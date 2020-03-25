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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)
    warehousing = models.IntegerField('入庫数', default=0)
    shipping = models.IntegerField('出庫数', default=0)
    created = models.DateTimeField('作成日', default=timezone.now)
    updated = models.DateTimeField('更新日', auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.location.name} - {self.parts.name}'
