
from django.conf.urls import include, url
from api import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('genres', views.GenreViewSet, 'genre')
router.register('phones', views.PhoneViewSet, 'phone')
router.register('books', views.BookViewSet, 'book')
router.register('courses', views.CourseViewSet, 'course')
router.register('students', views.StudentViewSet, 'student')

urlpatterns = [
    url('', include(router.urls))
]