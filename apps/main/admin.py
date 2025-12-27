from django.contrib import admin
from . import models


@admin.register(models.HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']
# Register your models here.
# admin.site.register(HomeSlider)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


@admin.register(models.ToDo)
class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('text', )}

# admin.site.register(models.Category)
# admin.site.register(models.ToDo)


admin.site.register(models.FAQ)




