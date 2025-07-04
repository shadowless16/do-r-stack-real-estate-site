from django.contrib import admin
from .models import Agent, AgentReview

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'agent_type', 'company', 'location', 'state', 'rating', 'experience_years', 'is_active', 'is_featured']
    list_filter = ['agent_type', 'state', 'is_active', 'is_featured', 'experience_years']
    search_fields = ['user__first_name', 'user__last_name', 'company', 'location']
    list_editable = ['is_active', 'is_featured']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Professional Details', {
            'fields': ('agent_type', 'company', 'license_number', 'experience_years')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'location', 'state')
        }),
        ('Profile', {
            'fields': ('bio', 'specialties', 'languages', 'profile_image')
        }),
        ('Status', {
            'fields': ('rating', 'total_reviews', 'is_active', 'is_featured')
        }),
    )

@admin.register(AgentReview)
class AgentReviewAdmin(admin.ModelAdmin):
    list_display = ['agent', 'reviewer_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['agent__user__first_name', 'agent__user__last_name', 'reviewer_name']
    readonly_fields = ['created_at']
