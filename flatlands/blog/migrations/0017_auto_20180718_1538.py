# Generated by Django 2.0.7 on 2018-07-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180718_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover_img',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
