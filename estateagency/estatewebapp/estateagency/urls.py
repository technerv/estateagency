from django.urls import path, include
from estateagency import views

app_name = 'estateagency'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('property/', views.property, name = 'property'),
    path('property/<str:pk>/', views.property_single, name = 'property_single'),
    path('show_all_properties/', views.show_all_properties, name = 'show_all_properties'),
    #url(r'^json/$', views.json, name = 'json'),


]
