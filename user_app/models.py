from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model to add additional fields and customization.
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # Specify custom related_names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    # Additional methods or customizations can be added here

    def __str__(self):
        """
        String representation of the User model.
        """
        return self.username


class PageVisit(models.Model):
    """
    Model to track user visits to different pages on the website.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_visits')
    page_name = models.CharField(max_length=100)
    visit_timestamp = models.DateTimeField(auto_now_add=True)
    visit_duration = models.DurationField(null=True, blank=True)
    is_conversion = models.BooleanField(default=False)

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the PageVisit model.
        """
        return f"{self.user.username} - {self.page_name} - {self.visit_timestamp}"
