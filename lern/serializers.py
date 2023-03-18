from rest_framework import serializers

from lern.models import Course, Lesson
from lern.validators import YouTubeLinkValidator
from payment.models import Payment, Subscribe


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        validators = [YouTubeLinkValidator(field='view_link')]
        fields = (
            'id',
            'lesson_title',
            'image',
            'description',
            'view_link',
            'course_set',
            'owner',
        )


class CourseSerializer(serializers.ModelSerializer):
    all_lesson = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set', required=False)

    class Meta:
        model = Course
        fields = (
            'id',
            'course_title',
            'image',
            'description',
            'all_lesson',
            'lessons',
            'owner',
            'subscription'
        )

    def get_all_lesson(self, instance):
        all_less = Lesson.objects.filter(course_set=instance)
        if all_less:
            return len(all_less)
        else:
            return 0

    def get_subscription(self, course):
        user = self.context['request'].user.id

        obj = Subscribe.objects.filter(course=course.id).filter(student=user)
        if obj:
            return 'Subscribed'
        return 'Unsubscribed'
