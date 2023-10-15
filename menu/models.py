from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Menu(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')

    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг', unique=True)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(MPTTModel):

    title = models.CharField(max_length=255, verbose_name='Название')

    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг', unique=True)

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='category', verbose_name='Меню')

    parent = TreeForeignKey('self', null=True, blank=True,
    on_delete=models.CASCADE, verbose_name='Родительская категория')

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.menu.slug + '-' + self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
