from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from lern.models import Course, Lesson
from lern.permissions import OwnerPerms, ModerPerms
from lern.serializers import CourseSerializer, LessonSerializer
from payment.tasks import subscribed_message
from payment.serializers import SubscribeSerializer
from users.models import User


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [ModerPerms | OwnerPerms]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            raise serializers.ValidationError('Модератор не может создавать уроки')
        else:
            # _mutable = request.data._mutable
            # set to mutable
            # request.data._mutable = True
            # сhange the values you want
            request.data['owner'] = request.user.pk
            # request.data._mutable = _mutable
            answer = super().create(request, *args, **kwargs)

        return answer

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):

        if self.request.user.is_staff:
            raise serializers.ValidationError('Модератор не может удалять курсы')
        else:
            request.data['owner'] = request.user.pk
            answer = super().create(request, *args, **kwargs)
        return answer

    def perform_update(self, serializer):
        self.object = serializer.save()
        subscribed_message.delay(self.object.pk)

    def perform_create(self, serializer):
        self.object = serializer.save()
        subscribed_message.delay(self.object.pk)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    permission_classes = [ModerPerms | OwnerPerms]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [OwnerPerms]
    serializer_class = LessonSerializer

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            raise serializers.ValidationError('Модератор не может создавать курсы')
        else:
            _mutable = request.data._mutable
            # set to mutable
            request.data._mutable = True
            # сhange the values you want

            request.data['owner'] = request.user.pk
            request.data._mutable = _mutable
            answer = super().create(request, *args, **kwargs)
            # set mutable flag back

        return answer


class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            raise serializers.ValidationError('Модератор не может удалять уроки')
        return queryset.filter(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(owner=self.request.user)
