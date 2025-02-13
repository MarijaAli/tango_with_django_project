from django.contrib import admin
from .models import Category
from .models import Page
from rango.models import UserProfile
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
