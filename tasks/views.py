from django.core.serializers import serialize
from django.utils.autoreload import raise_last_exception
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListCreateView(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):    #Only return tasks of logged-in user
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):    #Force ownership on creation
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):    #Only return tasks of logged-in user
        return Task.objects.filter(user=self.request.user)


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response({
            "message": "Login successful",
            "user_id": user.id,
            "username": user.username
        })

# With Manual API Views

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Task
# from .serializers import TaskSerializer
# from rest_framework.exceptions import PermissionDenied
#
# class TaskListCreateAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         tasks = Task.objects.filter(user=request.user)
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=201)
#
#         return Response(serializer.errors, status=400)

# class TaskDetailAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self, pk, user):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return None
#
#         if task.user != user:
#             raise PermissionDenied("Not your task")
#
#         return task
#
#     def get(self, request, pk):
#         task = self.get_object(pk, request.user)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         task = self.get_object(pk, request.user)
#         serializer = TaskSerializer(task, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         task = self.get_object(pk, request.user)
#         task.delete()
#         return Response({"message": "Deleted"})
