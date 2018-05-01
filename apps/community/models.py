from _datetime import datetime

from django.db import models


# Create your models here.

class Community(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name=u'小区ID')
    title = models.CharField(max_length=255, verbose_name=u'小区名称')
    link = models.CharField(unique=True, max_length=255, verbose_name=u'小区链接')
    district = models.CharField(max_length=255, verbose_name=u'所在行政区')
    bizcircle = models.CharField(max_length=255, verbose_name=u'所在商圈')
    taglist = models.CharField(db_column='tagList', max_length=255, verbose_name=u'附近地铁站')  # Field name made lowercase.
    onsale = models.CharField(max_length=255, verbose_name=u'在售')
    onrent = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'在租')
    year = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'建成年份')
    housetype = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'建筑类型')
    cost = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'物业费用')
    service = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'物业公司')
    company = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'开发商')
    building_num = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'楼栋总数')
    house_num = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'房屋总数')
    price = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'小区均价')
    # 不能使用datetime.now() 报错
    # 使用 auto_now_add 会使这个字段在admin无法编辑
    validdate = models.DateTimeField(default=datetime.now, verbose_name=u'更新时间')

    class Meta:
        # 不允许 Django to create, modify, and delete the table
        managed = False
        db_table = 'community_community'
        ordering = ('id',)
