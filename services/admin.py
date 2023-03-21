from django.contrib import admin

from .models import Service_list, Service_photos, Service_text

class ServiceListAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'description')
 list_display_links = ('id', 'title', 'description')
admin.site.register(Service_list, ServiceListAdmin)

class ServiceTextAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'subtitle', 'phone', 'description',)
 list_display_links = ('id', 'title', 'description')
admin.site.register(Service_text, ServiceTextAdmin)

class ServicePhotosAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'description', 'photo_main', 'photo_1', 'photo_2', 'photo_3')
  list_display_links = ('id', 'title', 'description')
  list_filter = ('photo_1', )
  list_editable = ('is_published',)
  search_fields = ('title', 'description')
  list_per_page = 20
admin.site.register(Service_photos, ServicePhotosAdmin)