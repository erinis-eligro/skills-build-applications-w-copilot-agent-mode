from rest_framework import serializers

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout


class ObjectIdStringMixin(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(getattr(obj, 'id', ''))


class TeamSerializer(ObjectIdStringMixin):
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe']
        read_only_fields = ['id']


class FitnessUserSerializer(ObjectIdStringMixin):
    class Meta:
        model = FitnessUser
        fields = ['id', 'name', 'email', 'team', 'total_points']
        read_only_fields = ['id']


class ActivitySerializer(ObjectIdStringMixin):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'points', 'performed_at']
        read_only_fields = ['id', 'performed_at']


class WorkoutSerializer(ObjectIdStringMixin):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'workout_name', 'intensity', 'scheduled_for']
        read_only_fields = ['id']


class LeaderboardSerializer(ObjectIdStringMixin):
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'score', 'rank']
        read_only_fields = ['id']
