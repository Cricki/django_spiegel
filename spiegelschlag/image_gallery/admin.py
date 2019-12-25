from django.contrib import admin

from .models import Category, Subcategory, Image

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 3


class ParentInline(admin.StackedInline):
    model = Category
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = [("name")]


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category")
    inlines = [ImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
