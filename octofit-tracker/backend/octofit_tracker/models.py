from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=80, unique=True)
    universe = models.CharField(max_length=20)

    class Meta:
        db_table = 'teams'

    def __str__(self) -> str:
        return self.name


class FitnessUser(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='users')
    total_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    points = models.IntegerField(default=0)
    performed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self) -> str:
        return f"{self.user.name} - {self.activity_type}"


class Workout(models.Model):
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE, related_name='workouts')
    workout_name = models.CharField(max_length=120)
    intensity = models.CharField(max_length=20)
    scheduled_for = models.DateField()

    class Meta:
        db_table = 'workouts'

    def __str__(self) -> str:
        return f"{self.user.name} - {self.workout_name}"


class Leaderboard(models.Model):
    user = models.OneToOneField(FitnessUser, on_delete=models.CASCADE, related_name='leaderboard_entry')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self) -> str:
        return f"#{self.rank} {self.user.name}"