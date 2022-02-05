from django.db import models
from django.utils import timezone

# Create your models here.

class Books(models.Model):
    Book_name = models.CharField('도서명', max_length=200, unique=True)
    Writer = models.CharField('저자', max_length=200)
    Publishing_date = models.DateTimeField('출판일',default=timezone.now)
    Price = models.IntegerField('가격',default=50)
    Intro_book = models.CharField('도서소개', max_length=200)

    def __str__(self):
    
        return self.Book_name 
# class writer(models.Model):
#     pass
#     
# class publish(models.Model):
#     pass
#     
# class price(models.Model):
#     pass
#     
# class intro_book(models.Model):
#     pass
    
