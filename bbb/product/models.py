from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    pro_name = models.CharField('상품명',max_length=200)
    pro_price = models.IntegerField('가격')
    pro_stock = models.IntegerField('재고수량',default=100)
    pro_img = models.ImageField('상품이미지',upload_to='products/%Y/%m/%d', blank=True)
    pro_desc = models.TextField('상품설명',blank=True)
    pro_hot = models.BooleanField('인기상품',default=False)
    pro_new = models.BooleanField('신규상품',default=False)
    pro_display = models.BooleanField('화면표시',default=True)
    pro_day = models.DateField('등록일',default=timezone.now)
    pro_like = models.IntegerField(default=0)

    def __str__(self):
        return self.pro_name

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.id])
