from modeltranslation.translator import register, TranslationOptions

from apps.posts.models import New, Category, Staff, Region


@register(New)
class NewTranslationOption(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Staff)
class StaffTranslation(TranslationOptions):
    fields = ('full_name', 'job')


@register(Region)
class RegionTranslation(TranslationOptions):
    fields = ('name',)
