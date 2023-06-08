from django.db import models
from django.conf import settings

class PaymentMethod(models.Model):
    """
    Model to represent the available payment methods.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    """
    Model to represent a payment made by a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.pk} - User: {self.user.username}, Amount: {self.amount}"

class Transaction(models.Model):
    """
    Model to represent a transaction associated with a payment.
    """
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.pk} - Payment: {self.payment}, Status: {self.status}"
