from django.db import models
from django.contrib.auth import get_user_model
from product_app.models import Product

User = get_user_model()



class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)

    # Additional fields or methods can be added here

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username} - {self.status}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Additional fields or methods can be added here

    def __str__(self):
        return f"Order #{self.order.pk} - {self.product.name} - {self.quantity}"
