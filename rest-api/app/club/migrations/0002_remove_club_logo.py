# Generated by Django 5.0 on 2023-12-30 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='logo',
        ),
    ]
