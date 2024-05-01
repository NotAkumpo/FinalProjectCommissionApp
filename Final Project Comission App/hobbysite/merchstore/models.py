from django.db import models
from django.urls import reverse
# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
           return self.name
           
    class Meta:
        ordering = ['name']
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True, related_name='product')
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
           return self.name

    def get_absolute_url(self):
           return reverse('merchstore:merchstore-detail', args=[self.pk])

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'