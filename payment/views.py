import datetime

import requests
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from lern.models import Course
from payment.models import Subscribe, Payment, PaymentLog
from payment.permisions import OwnerSubscribePerm
from payment.serializers import SubscribeSerializer, PaymentSerializer, PaymnetlogSerializer
from users.models import User


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            raise serializers.ValidationError('Модератор не может создавать оплаты')
        else:
            request.data['user'] = request.user.pk
            answer = super().create(request, *args, **kwargs)
            Subscribe.objects.create(subscribe_status=True)
            print(Subscribe.course)

        return answer


class SubscribeListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def post(self, request, *args, **kwargs):
        """Проверка данных на уникальность и создание экземпляра если данные уникальны"""
        data_student = User.objects.filter(email=request.data['student']).first()
        data_course = Course.objects.filter(course_title=request.data['course']).first()
        obj = self.queryset.filter(student=data_student).filter(course=data_course)
        if not obj:
            return self.create(request, *args, **kwargs)
        return Response(request.data, status=status.HTTP_200_OK)


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [OwnerSubscribePerm]


class PaymentAPIView(APIView):

    def get(self, *args, **kwargs):
        course_pk = self.kwargs.get('pk')
        course_item = get_object_or_404(Course, pk=course_pk)

        order_id = Payment.objects.create(
            payment_course=course_item,
            payment_sum=course_item.price,
            user=self.request.user,
            payment_date=datetime.datetime.now().date(),
            payment_type=Payment.PAYMENT_CARD
        )

        data_for_request = {
            "TerminalKey": settings.TERMINAL_KEY,
            "Amount": course_item.price,
            "OrderId": order_id.pk,
            "Receipt": {
                "Email": "a@test.ru",
                "Phone": "+79031234567",
                "EmailCompany": "b@test.ru",
                "Taxation": "osn",
                "Items": [
                    {
                        "Name": course_item.course_title,
                        "Price": course_item.price,
                        "Quantity": 1.00,
                        "Amount": course_item.price,
                        "PaymentMethod": "full_prepayment",
                        "PaymentObject": "commodity",
                        "Tax": "vat10",
                        "Ean13": "0123456789"
                    }
                ]
            }
        }

        response = requests.post('https://securepay.tinkoff.ru/v2/Init/', json=data_for_request)

        PaymentLog.objects.create(
            Success=response.json()['Success'],
            ErrorCode=response.json()['ErrorCode'],
            TerminalKey=response.json()['TerminalKey'],
            Status=response.json()['Status'],
            PaymentId=response.json()['PaymentId'],
            OrderId=response.json()['OrderId'],
            Amount=response.json()['Amount'],
            PaymentURL=response.json()['PaymentURL']
        )

        if response.json()['Success']:
            Subscribe.objects.create(
                student=self.request.user,
                course=course_item
            )

        print(response.json())
        return Response(
            {
                'url': response.json()['PaymentURL']
            }
        )


class PaymentlogList(generics.ListAPIView):
    serializer_class = PaymnetlogSerializer
    queryset = PaymentLog.objects.all()


class PaymentList(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
