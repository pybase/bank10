from django.db import models

# Create your models here.
class Bank(models.Model):
    img=models.ImageField(upload_to='gallery')
    name=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return self.name

class Members(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    name1=models.CharField(max_length=200)

    def __str__(self):
        return self.name


