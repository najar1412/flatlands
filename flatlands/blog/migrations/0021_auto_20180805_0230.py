# Generated by Django 2.0.7 on 2018-08-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20180804_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='strap',
            field=models.CharField(default='strap test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='strap',
            field=models.CharField(default='strap test', max_length=300),
            preserve_default=False,
        ),
    ]
