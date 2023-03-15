from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from lern.models import Course
from payment.models import Subscribe, Payment
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'user',
            'payment_date',
            'payment_course',
            'payment_sum',
            'payment_type'
        )


class SubscribeSerializer(serializers.ModelSerializer):
    student = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    course = SlugRelatedField(slug_field="course_title", queryset=Course.objects.all())

    class Meta:
        model = Subscribe
        fields = ('student', 'course')
