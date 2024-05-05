from django.contrib import admin
from .models import Team, Player, Match, FantasyTeam, Contest, ContestEntry

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')
    list_filter = ('country',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'age', 'gender', 'date_of_birth')
    search_fields = ('name', 'team__name')
    list_filter = ('team', 'age', 'gender')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'date', 'venue')
    search_fields = ('team1__name', 'team2__name', 'venue')
    list_filter = ('date', 'venue')

@admin.register(FantasyTeam)
class FantasyTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'captain', 'vice_captain')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_fee', 'prize_pool', 'start_time', 'end_time')
    search_fields = ('name',)
    list_filter = ('start_time', 'end_time')

@admin.register(ContestEntry)
class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'fantasy_team', 'score', 'ranking', 'winnings')
    search_fields = ('user__username', 'contest__name', 'fantasy_team__name')
    list_filter = ('contest',)
