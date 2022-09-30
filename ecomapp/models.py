from django.db import models

# Create your models here.
class ProductsData(models.Model):
    product_name=models.CharField(max_length=100)
    product_details=models.CharField(max_length=800)
    product_price=models.IntegerField()
    product_loc=models.CharField(max_length=200)
