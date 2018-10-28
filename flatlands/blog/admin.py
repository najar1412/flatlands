from django.contrib import admin
from .models import Post, Project, UsedSoftware, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(UsedSoftware)
admin.site.register(Tag)