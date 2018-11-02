from django.contrib import admin
from .models import Post, Project, UsedSoftware, Tag, Mailing_List

# Register your models here.

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(UsedSoftware)
admin.site.register(Tag)
admin.site.register(Mailing_List)