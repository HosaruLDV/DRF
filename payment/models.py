from django.db import models

from lern.models import Course
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    PAYMENT_CARD = 'card'
    PAYMENT_CASH = 'cash'
    PAYMENTS = (
        (PAYMENT_CARD, 'карта'),
        (PAYMENT_CASH, 'наличные')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='дата оплаты', null=True)
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_type = models.CharField(choices=PAYMENTS, default=PAYMENT_CARD, max_length=10, verbose_name='тип оплаты')

    def __str__(self):
        return f'{self.user},{self. payment_course},{self.payment_sum},'


class PaymentLog(models.Model):
    Success = models.BooleanField(verbose_name='успешность платежа')
    ErrorCode = models.CharField(max_length=250, verbose_name='код ошибки')
    TerminalKey = models.CharField(max_length=250, verbose_name='ключ терминала')
    Status = models.CharField(max_length=250, verbose_name='статус платежа')
    PaymentId = models.CharField(max_length=250, verbose_name='айди платежа')
    OrderId = models.CharField(max_length=250, verbose_name='айди заявки')
    Amount = models.IntegerField(verbose_name='сумма оплаты')
    PaymentURL = models.URLField(verbose_name='ссылка на оплату')
    PaymentDate = models.DateField(auto_now_add=True, verbose_name='дата создания')


class Subscribe(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')