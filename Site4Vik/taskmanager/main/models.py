from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=200)
    task = models.TextField('Наполнение')
class IMG(models.Model)
    image = models.ImageField(blank=True, upload_to='image/blog/%Y/%m/%d',
                              verbose_name='Ссылка картинок')
    taskm = models.ForeignKey(Task, related_name='image/blog/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'