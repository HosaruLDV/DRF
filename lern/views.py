from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from lern.models import Course, Lesson
from lern.permissions import OwnerPerms, ModerPerms
from lern.serializers import CourseSerializer, LessonSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [ModerPerms]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListView(generics.ListAPIView):
    permission_classes = [ModerPerms | OwnerPerms]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [ModerPerms | OwnerPerms]
    serializer_class = LessonSerializer
