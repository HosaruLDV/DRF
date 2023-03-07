from django.core.management import BaseCommand

from lern.models import Course, Lesson, Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        finance_data = [
            {
                "payment_sum": 1200.0,
                "payment_type": Payment.PAYMENT_CASH,
                "payment_course": Course.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
            {
                "payment_sum": 1344.54,
                "payment_type": Payment.PAYMENT_CARD,
                "payment_course": Course.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
            {
                "payment_sum": 1344.54,
                "payment_type": Payment.PAYMENT_CASH,
                "payment_course": Course.objects.filter(pk=2).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 344.05,
                "payment_type": Payment.PAYMENT_CASH,
                "payment_course": Lesson.objects.filter(pk=2).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 211.65,
                "payment_type": Payment.PAYMENT_CARD,
                "payment_course": Lesson.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 211.65,
                "payment_type": Payment.PAYMENT_CARD,
                "payment_course": Lesson.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
        ]
        payment_list = []
        Payment.objects.all().delete()

        for data in finance_data:
            payment_list.append(Payment(**data))

        Payment.objects.bulk_create(payment_list)