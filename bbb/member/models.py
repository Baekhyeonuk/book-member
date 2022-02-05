from django.db import models
from django.urls import reverse

# Create your models here.

class Mem(models.Model):
    Mem_id = models.CharField('회원아이디', max_length=200, unique=True)
    Mem_pwd = models.CharField('회원비밀번호', max_length=200)
    Mem_name = models.CharField('회원 이름', max_length=200)
    Mem_tel = models.CharField('연락처', max_length=200, null=True)
    Mem_addr = models.CharField('주소', max_length=200, null=True)
    Mem_img = models.FileField('사진',upload_to='member/%Y-%m-%d', null=True, blank='True', default='')

    def __str__(self):
        return self.Mem_id

    def get_absolute_url(self):
        return reverse('member:detail', args=[self.id])
    
    # def delete(self, *args, **kargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.Mem_img.name))
    #     super(Mem, self).delete(*args, **kargs)
