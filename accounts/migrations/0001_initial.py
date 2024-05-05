# Generated by Django 5.0.4 on 2024-05-05 20:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "entry_fee",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Entry Fee"
                    ),
                ),
                (
                    "prize_pool",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Prize Pool"
                    ),
                ),
                ("start_time", models.DateTimeField(verbose_name="Start Time")),
                ("end_time", models.DateTimeField(verbose_name="End Time")),
                (
                    "max_participants",
                    models.IntegerField(verbose_name="Max Participants"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="player_photos/",
                        verbose_name="Photo",
                    ),
                ),
                ("age", models.IntegerField(verbose_name="Age")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=10,
                        verbose_name="Gender",
                    ),
                ),
                ("date_of_birth", models.DateField(verbose_name="Date of Birth")),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="team_logos/",
                        verbose_name="Logo",
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Country")),
            ],
        ),
        migrations.CreateModel(
            name="FantasyTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                (
                    "captain",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="captain_teams",
                        to="accounts.player",
                        verbose_name="Captain",
                    ),
                ),
                (
                    "vice_captain",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="vice_captain_teams",
                        to="accounts.player",
                        verbose_name="Vice Captain",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContestEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Score",
                    ),
                ),
                (
                    "ranking",
                    models.IntegerField(blank=True, null=True, verbose_name="Ranking"),
                ),
                (
                    "winnings",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Winnings",
                    ),
                ),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.contest",
                        verbose_name="Contest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                (
                    "fantasy_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.fantasyteam",
                        verbose_name="Fantasy Team",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.team",
                verbose_name="Team",
            ),
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Date")),
                ("venue", models.CharField(max_length=100, verbose_name="Venue")),
                (
                    "team1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team1_matches",
                        to="accounts.team",
                        verbose_name="Team 1",
                    ),
                ),
                (
                    "team2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team2_matches",
                        to="accounts.team",
                        verbose_name="Team 2",
                    ),
                ),
            ],
        ),
    ]
