from rest_framework import viewsets

from api.models import Genre, Phone, Book, Course, Student, Phone
from api.serializers import (
    GenreSerializer, PhoneSerializer, BookSerializer,
    CourseSerializer, StudentSerializer
)

from django_restql.mixins import EagerLoadingMixin, QueryArgumentsMixin


class GenreViewSet(QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')
    filter_fields = {
        'id': ['exact', 'lt', 'gt'],
        'title': ['exact', 'contains'],
        'description': ['exact', 'contains']
    }


class PhoneViewSet(QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all().order_by('id')
    filter_fields = {
        'id': ['exact', 'lt', 'gt'],
        'number': ['exact', 'contains'],
        'type': ['exact'],
        'student': ['exact', 'lt', 'gt'],
    }


class BookViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('id')
    filter_fields = {
        'id': ['exact', 'lt', 'gt'],
        'title': ['exact', 'contains'],
        'author': ['exact', 'contains'],
        'genre__id': ['exact', 'lt', 'gt'],
        'genre__title': ['exact', 'contains'],
    }
    select_related = {
        "genre": "genre"
    }


class CourseViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')
    filter_fields = {
        'id': ['exact', 'lt', 'gt'],
        'name': ['exact', 'contains'],
        'code': ['exact', 'contains'],
    }
    prefetch_related = {
        "books": "books",
    }


class StudentViewSet(EagerLoadingMixin, QueryArgumentsMixin, viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('id')
    filter_fields = {
        'id': ['exact', 'lt', 'gt'],
        'name': ['exact', 'contains'],
        'age': ['exact', 'lt', 'gt'],
        'course__id': ['exact', 'lt', 'gt'],
        'course__name': ['exact', 'contains'],
        'course__code': ['exact', 'contains'],
    }
    select_related = {
        "course": "course"
    }
    prefetch_related = {
        "phone_numbers": "phone_numbers",
        "course.books": "course__books"
    }
