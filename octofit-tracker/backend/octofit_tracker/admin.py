from django.contrib import admin

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(FitnessUser)
class FitnessUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'team', 'total_points')
    list_filter = ('team',)
    search_fields = ('name', 'email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'points', 'performed_at')
    list_filter = ('activity_type',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'workout_name', 'intensity', 'scheduled_for')
    list_filter = ('intensity',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank', 'user', 'team', 'score')
    list_filter = ('team',)
    ordering = ('rank',)
