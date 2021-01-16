from django.db import models
from django.conf import settings
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    categoryName = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryName


class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    isbn = models.IntegerField(null=True, blank=True)
    pageCount = models.IntegerField(null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now,null=True, blank=True)
    thumbnailUrl = models.ImageField(upload_to='media/',null=True, blank=True)
    shortDescription = models.TextField(max_length=300, blank=True, null=True)
    longDescription = models.TextField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=200,null=True, blank=True)
    authors = models.ManyToManyField(
        Author, blank=True)
    categories = models.ManyToManyField(Category,  blank=True)

    def __str__(self):
        return self.title
