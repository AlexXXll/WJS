from django.contrib import admin
from .models import Task, TaskImage

class TaskImageInline(admin.TabularInline):
    model = TaskImage

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskImageInline]

    class Meta:
        model=Task

@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    pass