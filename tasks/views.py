from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer, UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        # For now, show all projects (no user filtering)
        return Project.objects.all()
        
        # TODO: Add back user filtering when we implement authentication
        # if self.request.user.is_authenticated:
        #     user = self.request.user
        #     return Project.objects.filter(
        #         Q(owner=user) | Q(members=user)
        #     ).distinct()
        # else:
        #     return Project.objects.all()
    
    def perform_create(self, serializer):
        # Set the current user as the project owner
        default_user = User.objects.first()
        serializer.save(owner=default_user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        # For now, show all tasks (no user filtering)
        return Task.objects.all()
        
        # TODO: Add back user filtering when we implement authentication
        # if self.request.user.is_authenticated:
        #     user = self.request.user
        #     return Task.objects.filter(
        #         Q(project__owner=user) | Q(project__members=user)
        #     ).distinct()
        # else:
        #     return Task.objects.all()
    
    def perform_create(self, serializer):
        # Set the current user as the task creator
        default_user = User.objects.first()
        serializer.save(created_by=default_user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # For now, show all comments (no user filtering)
        return Comment.objects.all()
        
        # TODO: Add back user filtering when we implement authentication
        # if self.request.user.is_authenticated:
        #     user = self.request.user
        #     return Comment.objects.filter(
        #         Q(task__project__owner=user) | Q(task__project__members=user)
        #     ).distinct()
        # else:
        #     return Comment.objects.all()
    
    def perform_create(self, serializer):
        # Set the current user as the comment author
        default_user = User.objects.first()
        print("Task creation data:", serializer.validated_data)
        serializer.save(user=default_user)