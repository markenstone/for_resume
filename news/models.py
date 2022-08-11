from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновленно')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото')
    is_published = models.BooleanField(default=True, verbose_name='публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='категория')

    def get_absolute_url(self):  # название согласно концвенции
        return reverse('show_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = "новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='наименование категории')

    def get_absolute_url(self):  # название согласно концвенции
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"
        ordering = ['title']
