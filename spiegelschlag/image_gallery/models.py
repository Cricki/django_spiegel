import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    parent_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_categories")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE)
    # tags = models.
    url = models.ImageField(upload_to='images')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
