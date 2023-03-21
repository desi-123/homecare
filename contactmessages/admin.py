from django.contrib import admin

from .models import ContactByMessage

class ContactByMessageAdmin(admin.ModelAdmin):
 list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'contact_date', 'message')
 list_display_links = ('id', 'first_name', 'last_name', 'message', 'phone')
 search_fields = ('first_name', 'email', 'phone')
 list_per_page = 25
admin.site.register(ContactByMessage, ContactByMessageAdmin)