from django.db import models


# Create your models here.

class Sellinfo(models.Model):
    houseid = models.CharField(db_column='houseID', primary_key=True, max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    housetype = models.CharField(max_length=255)
    square = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    totalprice = models.CharField(db_column='totalPrice', max_length=255)  # Field name made lowercase.
    unitprice = models.CharField(db_column='unitPrice', max_length=255)  # Field name made lowercase.
    dealdate = models.CharField(max_length=255, blank=True, null=True)
    updatedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sellinfo'
