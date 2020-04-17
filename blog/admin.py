from django.contrib import admin
from .models import Post, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    ordering = ['-published_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
