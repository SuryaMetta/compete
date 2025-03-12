from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# User Profiles with Access Levels
class Profile(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('participant', 'Participant'), ('judge', 'Judge')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='participant')
    rating = models.IntegerField(default=1200)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Competitive Programming Problems
class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    difficulty = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Submissions with Code Evaluation
class Submission(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Wrong Answer', 'Wrong Answer'), ('Time Limit Exceeded', 'Time Limit Exceeded')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"

# Contests with Scheduling
class Contest(models.Model):
    name = models.CharField(max_length=255)
    problems = models.ManyToManyField(Problem)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
