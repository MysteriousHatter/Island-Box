# Generated by Django 3.1.1 on 2020-12-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0015_auto_20201205_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel2',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=100000000)),
            ],
        ),
    ]