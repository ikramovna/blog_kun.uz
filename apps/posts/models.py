from django.db.models import (Model, CharField, TextField, ImageField, DateTimeField, CASCADE, ForeignKey, IntegerField)
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
    category = ForeignKey('Category', CASCADE)

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = CharField(_('name'), max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(Model):
    full_name = CharField(max_length=100)
    job = CharField(max_length=50)
    image = ImageField(upload_to='staff/images/')

    def __str__(self):
        return self.full_name


class Region(Model):
    name = CharField(max_length=100)
    blog = ForeignKey('New', CASCADE)

    def __str__(self):
        return self.name

