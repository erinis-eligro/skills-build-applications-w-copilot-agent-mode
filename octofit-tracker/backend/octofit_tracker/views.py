from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout
from octofit_tracker.serializers import (
    ActivitySerializer,
    FitnessUserSerializer,
    LeaderboardSerializer,
    TeamSerializer,
    WorkoutSerializer,
)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class UserViewSet(ModelViewSet):
    queryset = FitnessUser.objects.all().order_by('name')
    serializer_class = FitnessUserSerializer


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all().order_by('-performed_at')
    serializer_class = ActivitySerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all().order_by('scheduled_for')
    serializer_class = WorkoutSerializer


class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer


router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'users', UserViewSet, basename='users')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'teams': reverse('teams-list', request=request, format=format),
            'users': reverse('users-list', request=request, format=format),
            'activities': reverse('activities-list', request=request, format=format),
            'workouts': reverse('workouts-list', request=request, format=format),
            'leaderboard': reverse('leaderboard-list', request=request, format=format),
        }
    )
