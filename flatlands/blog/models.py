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
    strap = models.CharField(max_length=300)
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


class Post(models.Model):
    next_post = models.IntegerField(null=True, blank=True)
    previous_post = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    strap = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    cover_img = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=False)
    techspec = models.BooleanField(default=False)
    viewed = models.IntegerField(default=0)

    def tag_test(self):
        return str(self.tags)


    def __str__(self):
        return self.name
