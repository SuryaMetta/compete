from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Problem, Submission, Contest
from .forms import RegisterForm, SubmissionForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Competitive Programming Platform!</h1>")


# User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'challenges/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('problem_list')
    return render(request, 'challenges/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# List of Problems
@login_required
def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'challenges/problem_list.html', {'problems': problems})

# Problem Details and Submission
@login_required
def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect('leaderboard')
    else:
        form = SubmissionForm()
    return render(request, 'challenges/problem_detail.html', {'problem': problem, 'form': form})

# Real-time Leaderboard
@login_required
def leaderboard(request):
    top_users = Submission.objects.filter(status="Accepted").order_by('-created_at')[:10]
    return render(request, 'challenges/leaderboard.html', {'top_users': top_users})

# Active Contests
@login_required
def contest_list(request):
    contests = Contest.objects.filter(is_active=True)
    return render(request, 'challenges/contest_list.html', {'contests': contests})
