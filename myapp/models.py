# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=25)
    mainlanguage = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    def __str__(self):
        return self.name + " - " + self.mainlanguage

class Book (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    isbnNumber = models.CharField(max_length=30)
    publishdate = models.CharField(max_length=20)
    def __str__(self):
        return self.name


# Create your models here.
