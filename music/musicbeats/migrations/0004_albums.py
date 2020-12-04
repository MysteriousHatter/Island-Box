# Generated by Django 3.1.1 on 2020-12-03 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicbeats', '0003_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('albums_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=10000)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]