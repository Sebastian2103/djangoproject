# Generated by Django 5.0.1 on 2024-01-06 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_playerrating'),
        ('player', '0002_remove_player_assists_remove_player_goals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerrating',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match'),
        ),
        migrations.AlterField(
            model_name='playerrating',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player'),
        ),
    ]
