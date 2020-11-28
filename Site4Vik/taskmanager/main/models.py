from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=200)
    task = models.TextField('Наполнение')
    image = models.ImageField(blank=True, upload_to='image/', verbose_name='Ссылка картинки')
    file = models.FileField(blank=True, upload_to='Files/%Y/%m/%d', verbose_name='Ссылка файла')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
class TaskImage(models.Model):
    post = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='image/blog',
                              verbose_name='Ссылка картинки')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Фотография поста'
        verbose_name_plural = 'Фотографии поста'