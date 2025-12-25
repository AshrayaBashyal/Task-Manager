from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import TaskListCreateView, TaskDetailView, RegisterView, LoginView, MyProfileView, LogoutView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/", MyProfileView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view()),

]