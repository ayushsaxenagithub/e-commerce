from django.db import models


class Category(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the Category model.
        """
        return self.name


class Product(models.Model):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    photos = models.ManyToManyField('Photo', blank=True)
    videos = models.ManyToManyField('Video', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the Product model.
        """
        return self.name


class Photo(models.Model):
    """
    Model representing a product photo.
    """
    image = models.ImageField(upload_to='product_photos')

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the Photo model.
        """
        return self.image.name


class Video(models.Model):
    """
    Model representing a product video.
    """
    video_file = models.FileField(upload_to='product_videos')

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the Video model.
        """
        return self.video_file.name


class Tag(models.Model):
    """
    Model representing a product tag.
    """
    name = models.CharField(max_length=100)

    # Additional fields or methods can be added here

    def __str__(self):
        """
        String representation of the Tag model.
        """
        return self.name
