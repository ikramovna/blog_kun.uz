from django.core.validators import RegexValidator
from django.db.models import (Model, CharField, TextField, ImageField, DateTimeField, CASCADE, ForeignKey, IntegerField,
                              Index)
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class New(Model):
    title = CharField(_('title'), max_length=100)
    short_description = TextField(_('short_description'))
    long_description = TextField(_('long_description'))
    image = ImageField(upload_to='post/images/')
    created_at = DateTimeField(auto_now_add=True)
    views = IntegerField(default=0)
    category = ForeignKey('posts.Category', CASCADE, related_name='category_set')

    class Meta:
        indexes = [
            Index(fields=['title', 'short_description', 'long_description'])
        ]

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = CharField(max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Staff(Model):
    full_name = CharField(max_length=100)
    job = CharField(max_length=50)
    image = ImageField(upload_to='staff/images/')

    class Meta:
        indexes = [
            Index(fields=['full_name', 'job'])
        ]

    def __str__(self):
        return self.full_name

    # @property
    # def get_first_name(self):
    #     return self.full_name.split()[1]


class Region(Model):
    name = CharField(max_length=100)
    blog = ForeignKey('New', CASCADE)

    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    # phone_number = CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        indexes = [
            Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
