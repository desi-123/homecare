from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'author', 'body',)
 list_display_links = ('id', 'title', 'author')
 list_filter = ('id', )
 search_fields = ('title', 'body')
 list_per_page = 20
admin.site.register(Blog, BlogAdmin)