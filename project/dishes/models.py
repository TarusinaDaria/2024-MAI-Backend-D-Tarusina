from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(verbose_name="Название категории", max_length=20, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(verbose_name="Название блюда", max_length=50)
    ingredients = models.TextField(verbose_name='Ингредиенты')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.product_name
