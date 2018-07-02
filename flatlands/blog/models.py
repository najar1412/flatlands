import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=5000)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    tags = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def tag_list(self):
        return str(self.tags).split(' ')


    def __str__(self):
        return self.name
