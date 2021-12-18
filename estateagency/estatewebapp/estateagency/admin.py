from django.contrib import admin
from .models import Property, Agent

# Register your models here.
@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'location', 'property_type',
    'status','area','beds','baths','garage',
    'property_description','amenities','amount','image', 'date_created', 'agent_id',)

#admin.site.register(Property)
admin.site.register(Agent)
