from django.contrib import admin
from .models import services

class servicesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = services

#means that in admin pannel slug portion is also visible just beside of our model classes
# Register your models here.
admin.site.register(services,servicesAdmin)
