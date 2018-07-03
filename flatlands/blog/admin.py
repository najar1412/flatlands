from django.contrib import admin
from .models import Article, Project, UsedSoftware

# Register your models here.

admin.site.register(Article)
admin.site.register(Project)
admin.site.register(UsedSoftware)