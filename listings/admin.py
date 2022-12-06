


from django.contrib import admin
from .models import Listing, Profile #after making a model register it here

# Register your models here.
admin.site.register(Listing)
admin.site.register(Profile)

