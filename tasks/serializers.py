from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    is_overdue = serializers.ReadOnlyField()
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 
            'due_date', 'project', 'assigned_to', 'created_by',  # ← Added 'project' field
            'project_name', 'assigned_to_username', 'created_by_username',  # ← Added declared fields
            'comments', 'is_overdue', 'created_at', 'updated_at', 'completed_at'
        ]
        read_only_fields = [
            'created_at', 'updated_at', 'completed_at', 'is_overdue',
            'project_name', 'assigned_to_username', 'created_by_username'
        ]
    
    def validate_project(self, value):
        if not value.is_active:
            raise serializers.ValidationError("Cannot add tasks to an inactive project.")
        return value

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    task_count = serializers.ReadOnlyField()
    completed_task_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'owner', 'members', 'tasks',
            'task_count', 'completed_task_count', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']