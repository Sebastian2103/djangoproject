# Generated by Django 5.0 on 2024-01-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_favorite_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_teams',
        ),
    ]
