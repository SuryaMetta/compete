from django.urls import path # type: ignore
from .views import register, user_login, user_logout, problem_list, problem_detail, leaderboard, contest_list
from . import views
def home(request):
    return HttpResponse("<h1>Welcome to the Competitive Programming Platform!</h1>")
    
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', problem_list, name='problem_list'),
    path('problem/<int:problem_id>/', problem_detail, name='problem_detail'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('contests/', contest_list, name='contest_list'),
     path("admin/", admin.site.urls),
    path("", home, name="home"),  # Default homepage
    path("login/", views.custom_login, name="custom_login"),
]
