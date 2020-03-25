import os
import uuid
from django.db import models
from django.urls import reverse
from bbs_site.validators import validate_file_size


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
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200, blank=True)
    summary = models.TextField(max_length=1000, help_text="Enter description of the ad")

    def get_image_path(self, filename):
        """
        The function generates a file path
        """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('', filename)

    image = models.ImageField(upload_to=get_image_path, blank=True, validators=[validate_file_size])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])

    class Meta:
        ordering = ["id"]
