from rest_framework.routers import DefaultRouter
from django.urls import path

from lern.views import CourseViewSet, LessonListView, LessonCreateAPIView, LessonDeleteAPIView, LessonUpdateAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_list'),
    path('lesson/destroy/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_destroy'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
              ] + router.urls