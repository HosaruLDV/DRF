from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')
    view_link = models.CharField(max_length=500, verbose_name='ссылка на видео')
    course_set = models.ForeignKey(Course, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.lesson_title},{self.image},{self.description},{self.view_link}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

