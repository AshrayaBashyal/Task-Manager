from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RegisterView, LoginView, MyProfileView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/", MyProfileView.as_view()),

]