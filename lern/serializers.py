from rest_framework import serializers

from lern.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_title',
            'image',
            'description',
            'view_link',
            'course_set',
        )


class CourseSerializer(serializers.ModelSerializer):
    all_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set')

    class Meta:
        model = Course
        fields = (
            'course_title',
            'image',
            'description',
            'all_lesson',
            'lessons',
        )

    def get_all_lesson(self, instance):
        all_less = Lesson.objects.filter(course_set=instance)
        if all_less:
            return len(all_less)
        else:
            return 0
