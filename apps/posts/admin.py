from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.posts.models import Staff, New


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent')
#
#
# admin.site.register(Category, CategoryAdmin)


# class NewAdmin(admin.ModelAdmin):
#     list_display = ('title', 'short_description')
#
#
# admin.site.register(New, NewAdmin)


class NewAdmin(TranslatableAdmin):
    list_display = ('title', 'short_description', 'long_description')
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'long_description'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


admin.site.register(New, NewAdmin)



class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job')


admin.site.register(Staff, StaffAdmin)
