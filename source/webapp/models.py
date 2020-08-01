from django.db import models


class Book(models.Model):
    DEFAULT_STATUS = 'active'
    STATUS_CHOICES = [
        (DEFAULT_STATUS, 'активно'),
        ('blocked', 'заблокировано')
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    descriptions = models.TextField(max_length=2000, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, default=DEFAULT_STATUS, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return f'{self.name} - {self.status}'

