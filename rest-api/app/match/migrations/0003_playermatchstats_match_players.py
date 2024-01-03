# Generated by Django 5.0 on 2024-01-01 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_comment'),
        ('player', '0002_remove_player_assists_remove_player_goals_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerMatchStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', through='match.PlayerMatchStats', to='player.player'),
        ),
    ]