from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    """here we define the tables for the app in the admin panel """
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtors', 'state')
    list_display_links = ('id', 'title')
    list_filter = ('realtors',)
    list_editable = ('is_published', )
    search_fields = ('title', 'decription', 'address', 'city', 'state', 'zipcode','price',)
    list_per_page = 25
    


# here we add the admins to  listing model
admin.site.register(Listing, ListingAdmin)
