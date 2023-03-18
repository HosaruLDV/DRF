from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from lern.models import Lesson, Course


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='Hosaru@mail.ru')
        self.user.set_password('12345678')
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": "Hosaru@mail.ru", "password": "12345678"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_course_create(self):
        print(f'test1: Runed')
        response = self.client.post('/lern/course/',
                                    {
                                        "course_title": "Course5",
                                        "image": "test1",
                                        "description": "test1"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_create(self):
        print(f'test2: Runed')
        self.test_course_create()
        response = self.client.post('/lern/lesson/create/',
                                    {
                                        "lesson_title": "test22",
                                        "image": "test1",
                                        "description": "test1",
                                        "view_link": "https://www.youtube.com/watch?v=6zbgjwsCekI",
                                        "course_set": 1
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_destroy(self):
        print(f'test3: Runed')
        self.test_lesson_create()
        response = self.client.delete('/lern/lesson/destroy/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_udate(self):
        print(f'test4: Runed')
        self.test_lesson_create()
        response = self.client.patch('/lern/lesson/update/1/'
                                     , {
                                         "lesson_title": "lesson2218",
                                         "image": "test3",
                                         "description": "test3",
                                         "view_link": "https://www.youtube.com/watch?v=6zbgjwsCekI",
                                         "course_set": 1
                                     }
                                     )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_lessons_list(self):
        print(f'test5: Runed')
        self.test_lesson_create()
        """
            Тестирование получения списка студентов
        """
        response = self.client.get(
            '/lern/lesson/'
        )
        self.lesson = Lesson.objects.get(pk=1)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.lesson.id,
                    "lesson_title": self.lesson.lesson_title,
                    "image": self.lesson.image,
                    "description": self.lesson.description,
                    "view_link": self.lesson.view_link,
                    "course_set": self.lesson.course_set.pk,
                    "owner": self.lesson.owner.id,
                }
            ]
        )

    def test_subscribe(self):
        print(f'test6: Runed')
        self.test_course_create()

        response = self.client.post('/payment/subscribed/',
                                    {
                                        "student": "Hosaru@mail.ru",
                                        "course": "Course5"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscribe_status(self):
        print(f'test7: Runed')
        self.test_subscribe()

        response = self.client.get('/lern/course/')

        self.course = Course.objects.get(pk=1)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.course.id,
                    "course_title": self.course.course_title,
                    "image": self.course.image,
                    "description": self.course.description,
                    "all_lesson": 0,
                    "lessons": [],
                    "owner": self.course.owner.id,
                    "subscription": "Subscribed"
                }
            ]
        )
