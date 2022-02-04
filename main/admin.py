from django.contrib import admin

from .models import *


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ("image",)
    max_num = 5


@admin.register(Build)
class BuildsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInlineAdmin,
    ]


admin.site.register(Category)
admin.site.register(Image)
