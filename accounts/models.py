from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER = 'user'
    AGENT = 'agent'
    ACCOUNT_TYPE_CHOICES = [
        (USER, 'User'),
        (AGENT, 'Agent'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default=USER)

    def __str__(self):
        return f"{self.user.username} Profile"
