from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Price = models.FloatField()
    details = models.TextField()
    Description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.product_name