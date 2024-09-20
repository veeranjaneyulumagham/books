from django.db import models

# Create your models here.
class book(models.Model):
    book_id=models.CharField(max_length=100);
    bookname=models.CharField(max_length=100);
    photo=models.ImageField(upload_to='images');


