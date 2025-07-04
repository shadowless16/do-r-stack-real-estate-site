from django.urls import path
from . import views
from . import agent_views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/sale/', views.property_list, {'listing_type': 'sale'}, name='properties_sale'),
    path('properties/rent/', views.property_list, {'listing_type': 'rent'}, name='properties_rent'),
    path('shortlets/', views.property_list, {'listing_type': 'shortlet'}, name='shortlets'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    # Agent property management
    path('property/create/', agent_views.property_create, name='property_create'),
    path('property/<int:pk>/edit/', agent_views.property_edit, name='property_edit'),
    path('property/<int:pk>/delete/', agent_views.property_delete, name='property_delete'),
]
