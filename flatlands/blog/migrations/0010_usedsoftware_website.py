# Generated by Django 2.0.6 on 2018-07-03 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180703_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedsoftware',
            name='website',
            field=models.CharField(default='www.google.com', max_length=200),
            preserve_default=False,
        ),
    ]