from django.db import models
class Student(models.Model):
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    yas=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return f"{self.ad} {self.soyad}"
# Create your models here.
