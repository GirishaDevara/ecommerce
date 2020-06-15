from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    details = models.TextField(null=True)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/')
    image = models.URLField(max_length=2083)