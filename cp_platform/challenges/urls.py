from django.urls import path # type: ignore
from .views import register, user_login, user_logout, problem_list, problem_detail, leaderboard, contest_list

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', problem_list, name='problem_list'),
    path('problem/<int:problem_id>/', problem_detail, name='problem_detail'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('contests/', contest_list, name='contest_list'),
]
