# Generated by Django 2.0.6 on 2018-07-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_project_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_img',
            field=models.CharField(default='project_cover.jpg', max_length=200),
            preserve_default=False,
        ),
    ]
