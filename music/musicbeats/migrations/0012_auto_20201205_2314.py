# Generated by Django 3.1.1 on 2020-12-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0011_remove_song_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='music',
        ),
        migrations.AddField(
            model_name='channel',
            name='song',
            field=models.FileField(default='European-village-birds-sounds.mp3', upload_to='images'),
            preserve_default=False,
        ),
    ]
