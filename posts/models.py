from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):

    title = models.CharField(max_length=250, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    image = models.ImageField(upload_to='posts/', default='posts/default.png', verbose_name='изображение',
                              **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="автор", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateField(auto_now=True, verbose_name='дата редактирования')

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):

    text = models.TextField(verbose_name='текст')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="автор", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateField(auto_now=True, verbose_name='дата редактирования')

    def __str__(self):
        return f'{self.author} ({self.created_at})'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
