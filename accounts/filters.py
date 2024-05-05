import django_filters
from rest_framework import filters
from .models import Team, Player, Match, FantasyTeam, Contest, ContestEntry

class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = {
            'name': ['icontains'],
            'country': ['exact'],
        }

class PlayerFilter(django_filters.FilterSet):
    class Meta:
        model = Player
        fields = {
            'name': ['icontains'],
            'team__name': ['exact'],
            'age': ['exact', 'gte', 'lte'],
            'gender': ['exact'],
            'date_of_birth': ['year', 'month', 'day', 'gt', 'lt', 'gte', 'lte'],
        }

class MatchFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = {
            'team1__name': ['exact'],
            'team2__name': ['exact'],
            'date': ['year', 'month', 'day', 'gt', 'lt', 'gte', 'lte'],
            'venue': ['icontains'],
        }

class FantasyTeamFilter(django_filters.FilterSet):
    class Meta:
        model = FantasyTeam
        fields = {
            'name': ['icontains'],
            'user__username': ['exact'],
            'captain__name': ['exact'],
            'vice_captain__name': ['exact'],
        }

class ContestFilter(django_filters.FilterSet):
    class Meta:
        model = Contest
        fields = {
            'name': ['icontains'],
            'entry_fee': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'prize_pool': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'start_time': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt', 'lt', 'gte', 'lte'],
            'end_time': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt', 'lt', 'gte', 'lte'],
            'max_participants': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }

class ContestEntryFilter(django_filters.FilterSet):
    class Meta:
        model = ContestEntry
        fields = {
            'user__username': ['exact'],
            'contest__name': ['icontains'],
            'fantasy_team__name': ['icontains'],
            'score': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'ranking': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'winnings': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }

