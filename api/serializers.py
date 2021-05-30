from rest_framework import serializers
from api.models import Genre, Book, Course, Student, Phone

from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer


class GenreSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'url', 'title', 'description']


class PhoneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'url', 'number', 'type', 'student']


class BookSerializer(DynamicFieldsMixin, NestedModelSerializer):
    genre = NestedField(GenreSerializer, many=False, required=False, allow_null=True, accept_pk=True)

    class Meta:
        model = Book
        fields = ['id', 'url', 'title', 'author', 'genre']


class CourseSerializer(DynamicFieldsMixin, NestedModelSerializer):
    books = NestedField(BookSerializer, many=True, required=False)

    class Meta:
        model = Course
        fields = ['id', 'url', 'name', 'code', 'books']


class StudentSerializer(DynamicFieldsMixin, NestedModelSerializer):
    course = NestedField(CourseSerializer, allow_null=True, required=False)
    phone_numbers = NestedField(PhoneSerializer, many=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'age', 'course', 'phone_numbers']
