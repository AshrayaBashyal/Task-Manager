from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view())
    path("register/", RegisterAPIView.as_view())
    path("login/", LoginAPIView.as_view())

]