# Generated by Django 4.2.5 on 2023-11-29 16:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='tournament_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
