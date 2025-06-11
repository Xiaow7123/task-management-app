from django.contrib import admin
from .models import Project, Task, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'task_count', 'completed_task_count', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at', 'owner']
    search_fields = ['name', 'description']
    filter_horizontal = ['members']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'status', 'priority', 'due_date', 'is_overdue']
    list_filter = ['status', 'priority', 'created_at', 'project']
    search_fields = ['title', 'description']
    list_editable = ['status', 'priority']
    readonly_fields = ['created_at', 'updated_at', 'completed_at']
    
    def is_overdue(self, obj):
        return obj.is_overdue
    is_overdue.boolean = True
    is_overdue.short_description = 'Overdue'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['content']
    readonly_fields = ['created_at', 'updated_at']