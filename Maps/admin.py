from django.contrib import admin
from .models import Visitor

# Register your models here.
class VisitorAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'ip_address', 'country_full_name', 'region', 'city', 'latitude', 'longitude', 'visit_date')

    search_fields = ('country_full_name', 'region', 'city')

admin.site.register(Visitor, VisitorAdmin)