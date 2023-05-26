# Generated by Django 4.2.1 on 2023-05-26 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1_matches', to='tournaments.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2_matches', to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='tournaments.team')),
            ],
        ),
    ]
