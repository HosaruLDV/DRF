from rest_framework import serializers

from lern.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_title',
            'image',
            'description',
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_title',
            'image',
            'description',
            'view_link',
        )