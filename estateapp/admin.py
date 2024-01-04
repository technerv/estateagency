from django.contrib import admin
from .models import Property, Agent
from django.contrib.auth.models import User
#from accounts.models import User

# Register your models here.
@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('property_title','property_id', 'location', 'property_type',
    'status','area','beds','baths','garage',
    'property_description','amenities','amount','image', 'date_created', 'agent_id', 'user')

@admin.register(Agent)
class AgentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'email', 'phone', 'image')

#admin.site.register(User)
#admin.site.register(Agent)
