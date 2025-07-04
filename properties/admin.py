from django.contrib import admin
from .models import Property, PropertyImage, PropertyInquiry

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'listing_type', 'price', 'location', 'state', 'bedrooms', 'bathrooms', 'featured', 'available']
    list_filter = ['property_type', 'listing_type', 'state', 'featured', 'available', 'furnished']
    search_fields = ['title', 'location', 'description']
    list_editable = ['featured', 'available']
    inlines = [PropertyImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'agent')
        }),
        ('Property Details', {
            'fields': ('property_type', 'listing_type', 'price', 'location', 'state')
        }),
        ('Specifications', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet', 'parking_spaces', 'year_built')
        }),
        ('Features', {
            'fields': ('furnished', 'featured', 'available', 'min_stay_nights')
        }),
        ('Amenities (for Shortlets)', {
            'fields': ('wifi', 'pool', 'gym', 'security', 'generator', 'kitchen', 'air_conditioning'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'caption', 'is_main', 'created_at']
    list_filter = ['is_main', 'created_at']
    search_fields = ['property__title', 'caption']

@admin.register(PropertyInquiry)
class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = ['property', 'name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['property__title', 'name', 'email']
    readonly_fields = ['created_at']
