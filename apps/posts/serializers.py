from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.posts.models import (New, Category, Staff, Region)


# -------------Extract category by id and name---------------

# class NewCategoryModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')


# class NewModelSerializer(ModelSerializer):
#     category = SerializerMethodField()
#
#     def get_category(self, obj: New):
#         return model_to_dict(obj.category, ('id', 'name'))
#
#     class Meta:
#         model = New
#         fields = ('title', 'category')


# ----------------------------------------------------------
class NewModelSerializer(ModelSerializer):
    class Meta:
        model = New
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
        depth = 10


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


class SearchModelSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'short_description', 'long_description')


class SendEmailSerializer(Serializer):
    name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=55)
    message = CharField(max_length=500)
