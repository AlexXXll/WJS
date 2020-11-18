from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskImage
from .forms import TaskForm


def index_view(request):
    tasks = Task.objects.order_by('id')
    post = get_object_or_404(Task.id)
    photos = TaskImage.objects.filter(post=post)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks,
                                               'post':post,
                                               'photos':photos
                                               })

def detail_view(request, id):
    post = get_object_or_404(Task, id=id)
    photos = TaskImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })

def about_view(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'main/create.html', {'form': form, 'img_obj': img_obj})
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context, {'form': form})