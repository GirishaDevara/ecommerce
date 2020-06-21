from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.product_name}'

class Order(models.Model):
    order_items = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username }, items are { self.order_items.item_id}'
