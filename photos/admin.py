from django.contrib import admin
from .models import Location,Category,Image

# Register your models
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
