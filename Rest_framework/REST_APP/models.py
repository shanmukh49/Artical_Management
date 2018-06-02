from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    vote = models.IntegerField()
    
