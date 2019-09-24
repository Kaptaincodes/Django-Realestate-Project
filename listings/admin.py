from django.contrib import admin
from .models import Listing
# Register your models here.

# here we add the admins to  listing model
admin.site.register(Listing)