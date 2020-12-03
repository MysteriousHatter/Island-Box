# Generated by Django 3.1.1 on 2020-12-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0005_auto_20201203_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='artist_pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='albums',
            name='title',
            field=models.CharField(default='The Happy Song', max_length=1000),
            preserve_default=False,
        ),
    ]
