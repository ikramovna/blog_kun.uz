from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.posts.models import Staff, New, Category, Region


@admin.register(New)
class NewAdmin(TranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    pass


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    pass
