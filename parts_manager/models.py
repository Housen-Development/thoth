from django.db import models


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
    warehousing = models.IntegerField('入庫日', default=0)
    shipping = models.IntegerField('出庫日', default=0)
    input_date = models.DateTimeField('入力日')

    class Meta:
        ordering = ['parts__name']

    def __str__(self):
        return self.parts.name + '/' + self.location.name
