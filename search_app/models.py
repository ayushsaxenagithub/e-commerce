from django.db import models
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from product_app.models import Product
from user_app.models import User
from order_app.models import Order
from review_app.models import Review


class ProductSearch(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='search')
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('product__name', weight='A') + SearchVector('product__description', weight='B')
        super().save(*args, **kwargs)


class UserSearch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='search')
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('user__username', weight='A') + SearchVector('user__email', weight='B')
        super().save(*args, **kwargs)


class OrderSearch(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='search')
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('order__order_number', weight='A')
        super().save(*args, **kwargs)


class ReviewSearch(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='search')
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('review__content', weight='A')
        super().save(*args, **kwargs)
