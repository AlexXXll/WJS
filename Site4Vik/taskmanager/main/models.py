from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    image = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'