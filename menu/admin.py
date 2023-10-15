from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from menu.models import Menu, Category
from menu.forms import CategoryAdminForm

# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')

    fields = ('id', 'title', 'slug')
    readonly_fields = ('id',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):

    form = CategoryAdminForm

    list_display = ('tree_actions', 'id', 'indented_title', 'slug', 'parent', 'menu')
    list_display_links = ('indented_title', 'id')
    mptt_level_indent = 35

    fields = ('id', 'title', 'slug', 'parent', 'menu')
    readonly_fields = ('id',)
    ordering = ('menu', 'id')
    prepopulated_fields = {'slug': ('title',)}
