from datetime import date

from django.test import TestCase

from octofit_tracker.models import Activity, FitnessUser, Leaderboard, Team, Workout


class OctoFitApiTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='marvel team', universe='Marvel')
        self.user = FitnessUser.objects.create(
            name='Peter Parker',
            email='spiderman@octofit.dev',
            team=self.team,
            total_points=180,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration_minutes=40,
            points=40,
        )
        Workout.objects.create(
            user=self.user,
            workout_name='Hero HIIT',
            intensity='High',
            scheduled_for=date.today(),
        )
        Leaderboard.objects.create(
            user=self.user,
            team=self.team,
            score=180,
            rank=1,
        )

    def test_api_root_lists_all_collection_endpoints(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.json())
        self.assertIn('teams', response.json())
        self.assertIn('activities', response.json())
        self.assertIn('leaderboard', response.json())
        self.assertIn('workouts', response.json())

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)
