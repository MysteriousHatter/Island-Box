# Generated by Django 3.1.1 on 2020-12-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0019_auto_20201206_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='artist_pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]
