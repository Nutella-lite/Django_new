from django.db import models

class News(models.Model):
    title = models.CharField('Название', max_length=80)
    preview = models.CharField('Анонс', max_length=200, blank=True)
    text = models.TextField('Содержание')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    source = models.CharField('Источник', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'