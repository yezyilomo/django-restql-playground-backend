from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Genre, Phone, Book, Course, Student, Phone
from api.serializers import (
    GenreSerializer, PhoneSerializer, BookSerializer,
    CourseSerializer, StudentSerializer
)

from django_restql.mixins import EagerLoadingMixin, QueryArgumentsMixin


class GenreViewSet(QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')
    permission_classes = (AllowAny,)
    filter_fields = {
        'title': ['exact'],
    }


class PhoneViewSet(QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all().order_by('id')
    permission_classes = (AllowAny,)
    filter_fields = {
        'number': ['exact'],
        'type': ['exact'],
        'student': ['exact'],
    }


class BookViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('id')
    permission_classes = (AllowAny,)
    filter_fields = {
        'title': ['exact'],
        'author': ['exact'],
    }
    select_related = {
        "genre": "genre"
    }


class CourseViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')
    permission_classes = (AllowAny,)
    filter_fields = {
        'name': ['exact'],
        'code': ['exact'],
    }
    prefetch_related = {
        "books": "books",
    }


class StudentViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('id')
    permission_classes = (AllowAny,)
    filter_fields = {
        'name': ['exact'],
        'age': ['exact', 'lt', 'gt'],
        'course__code': ['exact'],
    }
    select_related = {
        "course": "course"
    }
    prefetch_related = {
        "phone_numbers": "phone_numbers",
        "course.books": "course__books"
    }
