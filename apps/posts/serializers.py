from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.posts.models import (New, Category, Staff, Region)


class NewModelSerializer(ModelSerializer):
    class Meta:
        model = New
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class StaffModelSerializer(ModelSerializer):
    class Meta:
        model = Staff
        exclude = ()


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ()


class LastBlogModelSerializer(ModelSerializer):
    class Meta:
        model = New
        exclude = ()


class SendEmailSerializer(Serializer):
    name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=55)
    message = CharField(max_length=500)
