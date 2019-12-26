from django.contrib import admin

from .models import Category, Subcategory, Image, Tag

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

class TagInline(admin.StackedInline):
    model = Tag
    extra = 3

class ImageAdmin(admin.ModelAdmin):
    list_display = [("name")]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [("name")]

class TagAdmin(admin.ModelAdmin):
    list_display = [("name")]

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category")
    inlines = [ImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tag, TagAdmin)
