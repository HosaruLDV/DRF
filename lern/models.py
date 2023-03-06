from django.db import models


class Course(models.Model):
    course_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.course_title},{self.image},{self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')
    view_link = models.CharField(max_length=500, verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.course_title},{self.image},{self.description},{self.view_link}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
