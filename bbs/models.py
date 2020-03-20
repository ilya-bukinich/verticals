import os
from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Category(models.Model):
    """
    The model represents an ad category.
    """
    name = models.CharField(max_length=200, help_text="Enter an advert category (e.g. Electronic, Clothes etc.)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Advert(models.Model):
    """
    Model presents an ad
    """
    title = models.CharField(max_length=200)
    create_datetime = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, help_text="Select a category for this ad")
    author = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter description of the ad")

    def get_image_path(self, filename):
        """
        The function generates a file path
        """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('', filename)

    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])

    class Meta:
        ordering = ["id"]

    display_category.short_description = 'Category'
