# Generated by Django 4.2.5 on 2023-11-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_tournament_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tournament_images/'),
        ),
    ]
