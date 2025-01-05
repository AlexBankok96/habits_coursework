from django.db import models
from django.core.exceptions import ValidationError
from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


def validate_duration(value):
    if value > 120:
        raise ValidationError('Длительность не может быть больше 120 секунд.')


class Habits(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневная'),
        ('weekly', 'Еженедельная'),
        ('monthly', 'Ежемесячная'),
    ]

    IS_GOOD_CHOICES = [
        (True, 'Приятная'),
        (False, 'Нет'),
    ]

    PUBLIC_CHOICES = [
        (True, 'Публичная'),
        (False, 'Нет'),
    ]

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.TimeField(verbose_name='Время, когда надо выполнить привычку')
    action = models.CharField(max_length=100, verbose_name='Действие, которое надо сделать')
    duration = models.IntegerField(validators=[validate_duration], verbose_name='Продолжительность в секундах')
    period = models.CharField(
        max_length=10, choices=PERIOD_CHOICES, default='daily', verbose_name='Периодичность'
    )
    is_good = models.BooleanField(default=True, verbose_name='Приятная', choices=IS_GOOD_CHOICES)
    is_public = models.BooleanField(default=True, verbose_name='Публичная', choices=PUBLIC_CHOICES)
    related = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name='Связанная с другой привычкой', **NULLABLE
    )
    prize = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-id']
