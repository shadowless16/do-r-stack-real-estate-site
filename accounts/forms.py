from django import forms
from .models import UserProfile
from agents.models import Agent

class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'company', 'license_number', 'phone', 'email', 'location', 'state', 'bio',
            'experience_years', 'specialties', 'languages', 'profile_image',
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'specialties': forms.TextInput(attrs={'placeholder': 'Comma-separated'}),
            'languages': forms.TextInput(attrs={'placeholder': 'Comma-separated'}),
        }
