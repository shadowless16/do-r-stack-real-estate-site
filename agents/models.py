from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    AGENT_TYPES = [
        ('agent', 'Real Estate Agent'),
        ('developer', 'Property Developer'),
        ('manager', 'Property Manager'),
        ('advisor', 'Investment Advisor'),
    ]
    
    STATES = [
        ('lagos', 'Lagos'),
        ('abuja', 'Abuja'),
        ('kano', 'Kano'),
        ('port-harcourt', 'Port Harcourt'),
        ('ibadan', 'Ibadan'),
        ('kaduna', 'Kaduna'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent_type = models.CharField(max_length=20, choices=AGENT_TYPES, default='agent')
    company = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=STATES)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField()
    specialties = models.CharField(max_length=500, help_text="Comma-separated specialties")
    languages = models.CharField(max_length=200, help_text="Comma-separated languages")
    profile_image = models.ImageField(upload_to='agent_profiles/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-rating', '-created_at']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.company}"

    def get_specialties_list(self):
        return [s.strip() for s in self.specialties.split(',') if s.strip()]

    def get_languages_list(self):
        return [l.strip() for l in self.languages.split(',') if l.strip()]

    def get_properties_count(self):
        return self.properties.filter(available=True).count()


class AgentReview(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review for {self.agent.user.get_full_name()} - {self.rating} stars"
