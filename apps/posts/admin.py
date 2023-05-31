from django.contrib import admin

from apps.posts.models import Category, New, Staff


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Category, CategoryAdmin)


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')


admin.site.register(New, NewAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job')


admin.site.register(Staff, StaffAdmin)
