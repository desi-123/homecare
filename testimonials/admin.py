from django.contrib import admin
from .models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'subtitle', 'is_published', 'description', 'body', 'post_date')
  list_display_links = ('id', 'title', 'description', 'body')
  list_filter = ('post_date', )
  list_editable = ('is_published',)
  search_fields = ('title', 'description')
  list_per_page = 20
admin.site.register(Testimonials, TestimonialsAdmin)