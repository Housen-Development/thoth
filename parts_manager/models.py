from django.db import models
from django.urls import reverse


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
    warehousing = models.PositiveIntegerField('入庫数', default=0)
    shipping = models.PositiveIntegerField('出庫数', default=0)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['parts__code']

    def __str__(self):
        return f'{self.location.name} - {self.parts.name}'

    def get_absolute_url(self):
        return reverse()
