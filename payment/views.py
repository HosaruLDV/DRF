from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.response import Response

from lern.models import Course
from payment.models import Subscribe
from payment.permisions import OwnerSubscribePerm
from payment.serializers import SubscribeSerializer, PaymentSerializer
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
