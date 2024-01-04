from django.conf.urls import url, include
from estateapp import views
from estateapp.views import *

app_name = 'estateapp'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^property/$', views.property, name = 'property'),
    url(r'^property/(?P<id>\d+)/$', views.property_single, name = 'property_single'),
    url(r'^show_all_properties/$', views.show_all_properties, name = 'show_all_properties'),
    url(r'^json/$', views.json, name = 'json'),

    #Django Auth
    url(r'^accounts/register/$', views.register, name = 'register'),
    url(r'^accounts/logout/$', views.logout_view, name = 'logout'),

]
