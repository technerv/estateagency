import django_filters
#from django_filters import DateFilter


from .models import *

class PropertyFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['property_id', 'property_description', 'amenities', 'image', 'date_created', 'agent_id']
