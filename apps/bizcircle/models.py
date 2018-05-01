from django.db import models


# Create your models here.

class Bizcircle(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u'商圈ID')
    district = models.CharField(max_length=255, verbose_name=u'所在行政区')
    bizcircle = models.CharField(max_length=255, verbose_name=u'商圈名称')

    class Meta:
        ordering = ('bizcircle',)
