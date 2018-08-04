from django.contrib import admin
from .models import Article, Project, UsedSoftware, Tag

# Register your models here.

admin.site.register(Article)
admin.site.register(Project)
admin.site.register(UsedSoftware)
admin.site.register(Tag)