# Generated by Django 3.1.1 on 2020-12-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0002_channel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images')),
                ('tags', models.CharField(max_length=100)),
                ('songs', models.FileField(upload_to='images')),
            ],
        ),
    ]