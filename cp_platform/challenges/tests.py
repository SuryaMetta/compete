from django.test import TestCase # type: ignore
from .models import Problem

class ProblemModelTest(TestCase):
    def setUp(self):
        self.problem = Problem.objects.create(
            title="Sample Problem",
            description="Solve this problem.",
            input_format="Two integers",
            output_format="Sum of integers",
            sample_input="3 4",
            sample_output="7",
            difficulty="Easy"
        )

    def test_problem_creation(self):
        """Test if the problem is created successfully."""
        self.assertEqual(self.problem.title, "Sample Problem")
        self.assertEqual(self.problem.difficulty, "Easy")
