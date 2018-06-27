# Generated by Django 2.0.6 on 2018-06-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(default='here are some test tags', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.CharField(max_length=5000),
        ),
    ]
