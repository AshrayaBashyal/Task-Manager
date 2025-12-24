from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




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
