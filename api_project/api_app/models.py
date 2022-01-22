from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return "{}".format(self.category)

class Product(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    cash_on_delivery = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return "{}".format(self.name)

