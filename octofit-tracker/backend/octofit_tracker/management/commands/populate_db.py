from datetime import date, timedelta

from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        FitnessUser.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(name='marvel team', universe='Marvel')
        dc_team = Team.objects.create(name='dc team', universe='DC')

        users = [
            FitnessUser.objects.create(
                name='Peter Parker',
                email='spiderman@octofit.dev',
                team=marvel_team,
                total_points=180,
            ),
            FitnessUser.objects.create(
                name='Tony Stark',
                email='ironman@octofit.dev',
                team=marvel_team,
                total_points=220,
            ),
            FitnessUser.objects.create(
                name='Bruce Wayne',
                email='batman@octofit.dev',
                team=dc_team,
                total_points=210,
            ),
            FitnessUser.objects.create(
                name='Diana Prince',
                email='wonderwoman@octofit.dev',
                team=dc_team,
                total_points=230,
            ),
        ]

        for user in users:
            Activity.objects.create(
                user=user,
                activity_type='Running',
                duration_minutes=40,
                points=40,
            )
            Activity.objects.create(
                user=user,
                activity_type='Strength Training',
                duration_minutes=30,
                points=50,
            )

            Workout.objects.create(
                user=user,
                workout_name='Hero HIIT',
                intensity='High',
                scheduled_for=date.today() + timedelta(days=1),
            )

        ranked_users = sorted(users, key=lambda item: item.total_points, reverse=True)
        for rank, user in enumerate(ranked_users, start=1):
            Leaderboard.objects.create(
                user=user,
                team=user.team,
                score=user.total_points,
                rank=rank,
            )

        self.stdout.write(self.style.SUCCESS('octofit_db 샘플 데이터 적재 완료'))
