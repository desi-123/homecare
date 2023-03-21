from django.contrib import admin

from .models import About, About_team, Home, Contact
class AboutAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'name', 'photo_about', 'description_one', 'description_two')
 list_display_links = ('id', 'title', 'description_one', 'description_two', 'name')
 list_filter = ('title', )
 search_fields = ('title',)
 list_per_page = 20
admin.site.register(About, AboutAdmin)

class AboutTeamAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'name', 'photo_team', 'description',)
 list_display_links = ('id', 'title', 'description')
admin.site.register(About_team, AboutTeamAdmin)

class HomeAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'subtitle', 'description_one', 'description_two', 'description_three', 'description_four')
  list_display_links = ('id', 'title', 'description_one', 'description_two', 'description_three', 'subtitle', 'description_four')
  list_filter = ('title', )
  search_fields = ('title',)
  list_per_page = 20
admin.site.register(Home, HomeAdmin)


class ContactAdmin(admin.ModelAdmin):
 list_display = ('email', 'phone', 'description_one', 'description_two', 'description_three', 'address', 'city', 'state', 'zipcode')
 list_display_links = ('description_one', 'description_two', 'description_three', 'address', 'city', 'state', 'zipcode')
 search_fields = ('state', 'city', 'description_one')
 list_per_page = 25

admin.site.register(Contact, ContactAdmin)
