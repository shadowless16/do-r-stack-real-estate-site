import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
import django
django.setup()

from django.contrib.auth.models import User
from agents.models import Agent

def create_missing_agents():
    # Find all users with userprofile.account_type == 'agent' but no Agent object
    from accounts.models import UserProfile
    agent_profiles = UserProfile.objects.filter(account_type='agent')
    created = 0
    for profile in agent_profiles:
        user = profile.user
        if not Agent.objects.filter(user=user).exists():
            Agent.objects.create(
                user=user,
                company='',
                license_number=f'AGENT-{user.id}',
                phone='',
                email=user.email,
                location='',
                state='lagos',
                bio='',
                experience_years=0,
                specialties='',
                languages=''
            )
            created += 1
    print(f"Created {created} missing Agent objects.")

if __name__ == "__main__":
    create_missing_agents()
