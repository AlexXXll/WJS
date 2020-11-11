from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=200)
    task = models.TextField('Наполнение')
    image = models.ImageField(blank=True, upload_to='image/blog',
                               verbose_name='Ссылка картинки')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class IMG(models.Model):
    images = models.ImageField(blank=True, upload_to='image/blog',
                              verbose_name='Ссылка картинок')
    taskm = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='image/blog')