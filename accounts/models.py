from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

GENDER_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
]

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True, verbose_name=_('Logo'))
    country = models.CharField(max_length=100, verbose_name=_('Country'))

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_('Team'))
    photo = models.ImageField(upload_to='player_photos/', null=True, blank=True, verbose_name=_('Photo'))
    age = models.IntegerField(verbose_name=_('Age'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'))

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE, verbose_name=_('Team 1'))
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE, verbose_name=_('Team 2'))
    date = models.DateField(verbose_name=_('Date'))
    venue = models.CharField(max_length=100, verbose_name=_('Venue'))

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"

class FantasyTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    captain = models.ForeignKey(Player, related_name='captain_teams', on_delete=models.SET_NULL, null=True, verbose_name=_('Captain'))
    vice_captain = models.ForeignKey(Player, related_name='vice_captain_teams', on_delete=models.SET_NULL, null=True, verbose_name=_('Vice Captain'))

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Entry Fee'))
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Prize Pool'))
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'))
    max_participants = models.IntegerField(verbose_name=_('Max Participants'))

    def __str__(self):
        return self.name

class ContestEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name=_('Contest'))
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, verbose_name=_('Fantasy Team'))
    score = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_('Score'))
    ranking = models.IntegerField(null=True, blank=True, verbose_name=_('Ranking'))
    winnings = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_('Winnings'))

    def __str__(self):
        return f"{self.user.username} - {self.contest.name}"