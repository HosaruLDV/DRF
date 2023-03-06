from rest_framework.routers import DefaultRouter
from django.urls import path

from lern.views import CourseViewSet, LessonListView, LessonCreateAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_list'),
              ] + router.urls