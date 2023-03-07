from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.course_title},{self.image},{self.description},'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=250, verbose_name='название')
    image = models.CharField(max_length=250, verbose_name="превью")
    description = models.CharField(max_length=500, verbose_name='описание')
    view_link = models.CharField(max_length=500, verbose_name='ссылка на видео')
    course_set = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson_title},{self.image},{self.description},{self.view_link}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    PAYMENT_CARD = 'card'
    PAYMENT_CASH = 'cash'
    PAYMENTS = (
        (PAYMENT_CARD, 'карта'),
        (PAYMENT_CASH, 'наличные')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='дата оплаты', null=True)
    payment_course = models.CharField(max_length=250, verbose_name='название оплаченного курса')
    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_type = models.CharField(choices=PAYMENTS, default=PAYMENT_CARD, max_length=10, verbose_name='тип оплаты')
