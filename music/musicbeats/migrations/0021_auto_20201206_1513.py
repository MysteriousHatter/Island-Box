# Generated by Django 3.1.1 on 2020-12-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0020_auto_20201206_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='channel_id',
        ),
        migrations.AddField(
            model_name='channel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]