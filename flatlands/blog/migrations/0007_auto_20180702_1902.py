# Generated by Django 2.0.6 on 2018-07-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_project_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.CharField(default='project content blalbalb a lalb alb jkhfkjhdgkjdhg kjdhfg kjdfgh kjd', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(default='here are some tags', max_length=200),
            preserve_default=False,
        ),
    ]
