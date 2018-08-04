import datetime

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=5000)
    tags = models.ManyToManyField(Tag, blank=True)
    cover_img = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    repo = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name


class UsedSoftware(models.Model):
    name = models.CharField(max_length=200)
    small_logo = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project, blank=True)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    cover_img = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=False)
    techspec = models.BooleanField(default=False)

    def tag_test(self):
        return str(self.tags)


    def __str__(self):
        return self.name
