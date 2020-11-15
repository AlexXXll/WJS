from django.contrib import admin
from .models import Task, TaskImage

class TaskImageAdmin(admin.StackedInline):
    model = TaskImage

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskImageAdmin]

    class Meta:
        model=Task

@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    pass