#!/usr/bin/env python
"""
Script to create sample data for the Django Real Estate application.
Run this script after running migrations to populate the database with sample data.

Usage: python manage.py shell < scripts/create_sample_data.py
"""

import os
import django
from decimal import Decimal
from django.contrib.auth.models import User

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate.settings')
django.setup()

from properties.models import Property, PropertyImage
from agents.models import Agent, AgentReview

def create_sample_data():
    print("Creating sample data...")
    
    # Create sample users for agents
    users_data = [
        {'username': 'adebayo_johnson', 'first_name': 'Adebayo', 'last_name': 'Johnson', 'email': 'adebayo@example.com'},
        {'username': 'chioma_okafor', 'first_name': 'Chioma', 'last_name': 'Okafor', 'email': 'chioma@example.com'},
        {'username': 'fatima_abdullahi', 'first_name': 'Fatima', 'last_name': 'Abdullahi', 'email': 'fatima@example.com'},
        {'username': 'emeka_nwankwo', 'first_name': 'Emeka', 'last_name': 'Nwankwo', 'email': 'emeka@example.com'},
        {'username': 'aisha_mohammed', 'first_name': 'Aisha', 'last_name': 'Mohammed', 'email': 'aisha@example.com'},
    ]
    
    users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': user_data['email'],
                'is_active': True
            }
        )
        users.append(user)
        if created:
            print(f"Created user: {user.get_full_name()}")
    
    # Create sample agents
    agents_data = [
        {
            'user': users[0],
            'agent_type': 'agent',
            'company': 'Lagos Premium Properties',
            'license_number': 'LPP001',
            'phone': '+234 801 234 5678',
            'email': 'adebayo@lagospremium.com',
            'location': 'Victoria Island, Lagos',
            'state': 'lagos',
            'bio': 'Experienced real estate agent specializing in luxury properties in Lagos.',
            'experience_years': 8,
            'specialties': 'Luxury Homes, Commercial Properties',
            'languages': 'English, Yoruba',
            'rating': Decimal('4.9'),
            'total_reviews': 127,
            'is_featured': True,
        },
        {
            'user': users[1],
            'agent_type': 'developer',
            'company': 'Abuja Urban Developments',
            'license_number': 'AUD002',
            'phone': '+234 802 345 6789',
            'email': 'chioma@abujaurbandevelopments.com',
            'location': 'Maitama, Abuja',
            'state': 'abuja',
            'bio': 'Property developer with focus on sustainable urban development.',
            'experience_years': 12,
            'specialties': 'New Developments, Investment Properties',
            'languages': 'English, Igbo',
            'rating': Decimal('4.8'),
            'total_reviews': 89,
            'is_featured': True,
        },
        {
            'user': users[2],
            'agent_type': 'agent',
            'company': 'Northern Nigeria Homes',
            'license_number': 'NNH003',
            'phone': '+234 803 456 7890',
            'email': 'fatima@northernhomes.com',
            'location': 'Nassarawa GRA, Kano',
            'state': 'kano',
            'bio': 'Residential specialist helping families find their perfect homes.',
            'experience_years': 6,
            'specialties': 'First-time Buyers, Family Homes',
            'languages': 'English, Hausa',
            'rating': Decimal('4.9'),
            'total_reviews': 156,
            'is_featured': True,
        },
        {
            'user': users[3],
            'agent_type': 'agent',
            'company': 'Port Harcourt Business Properties',
            'license_number': 'PHBP004',
            'phone': '+234 804 567 8901',
            'email': 'emeka@phbusinessproperties.com',
            'location': 'GRA Phase 2, Port Harcourt',
            'state': 'port-harcourt',
            'bio': 'Commercial real estate specialist in the oil and gas hub of Nigeria.',
            'experience_years': 10,
            'specialties': 'Office Spaces, Retail Properties',
            'languages': 'English, Igbo',
            'rating': Decimal('4.7'),
            'total_reviews': 73,
            'is_featured': False,
        },
        {
            'user': users[4],
            'agent_type': 'advisor',
            'company': 'Elite Properties Nigeria',
            'license_number': 'EPN005',
            'phone': '+234 805 678 9012',
            'email': 'aisha@eliteproperties.ng',
            'location': 'Ikoyi, Lagos',
            'state': 'lagos',
            'bio': 'Luxury property consultant and investment advisor.',
            'experience_years': 15,
            'specialties': 'Luxury Estates, High-end Rentals',
            'languages': 'English, Arabic',
            'rating': Decimal('4.9'),
            'total_reviews': 203,
            'is_featured': True,
        },
    ]
    
    agents = []
    for agent_data in agents_data:
        agent, created = Agent.objects.get_or_create(
            user=agent_data['user'],
            defaults=agent_data
        )
        agents.append(agent)
        if created:
            print(f"Created agent: {agent.user.get_full_name()}")
    
    # Create sample properties
    properties_data = [
        {
            'title': 'Luxury 4-Bedroom Duplex',
            'description': 'Beautiful modern duplex in the heart of Lekki Phase 1 with contemporary finishes and premium amenities.',
            'property_type': 'duplex',
            'listing_type': 'sale',
            'price': Decimal('85000000'),
            'location': 'Lekki Phase 1, Lagos',
            'state': 'lagos',
            'bedrooms': 4,
            'bathrooms': 3,
            'square_feet': 2500,
            'parking_spaces': 2,
            'year_built': 2022,
            'furnished': False,
            'featured': True,
            'agent': agents[0],
        },
        {
            'title': 'Modern 3-Bedroom Apartment',
            'description': 'Stylish apartment in Victoria Island with stunning city views and modern amenities.',
            'property_type': 'apartment',
            'listing_type': 'sale',
            'price': Decimal('45000000'),
            'location': 'Victoria Island, Lagos',
            'state': 'lagos',
            'bedrooms': 3,
            'bathrooms': 2,
            'square_feet': 1800,
            'parking_spaces': 1,
            'year_built': 2021,
            'furnished': False,
            'featured': False,
            'agent': agents[0],
        },
        {
            'title': 'Executive 5-Bedroom Villa',
            'description': 'Exclusive villa on Banana Island with private beach access and luxury amenities.',
            'property_type': 'villa',
            'listing_type': 'sale',
            'price': Decimal('250000000'),
            'location': 'Banana Island, Lagos',
            'state': 'lagos',
            'bedrooms': 5,
            'bathrooms': 4,
            'square_feet': 4000,
            'parking_spaces': 3,
            'year_built': 2023,
            'furnished': True,
            'featured': True,
            'agent': agents[4],
        },
        {
            'title': 'Furnished 3-Bedroom Apartment',
            'description': 'Fully furnished apartment perfect for executives and expatriates.',
            'property_type': 'apartment',
            'listing_type': 'rent',
            'price': Decimal('2500000'),
            'location': 'Victoria Island, Lagos',
            'state': 'lagos',
            'bedrooms': 3,
            'bathrooms': 2,
            'square_feet': 1500,
            'parking_spaces': 1,
            'year_built': 2020,
            'furnished': True,
            'featured': True,
            'agent': agents[0],
        },
        {
            'title': 'Executive 4-Bedroom Duplex',
            'description': 'Spacious duplex in a serene environment perfect for families.',
            'property_type': 'duplex',
            'listing_type': 'rent',
            'price': Decimal('4000000'),
            'location': 'Lekki Phase 1, Lagos',
            'state': 'lagos',
            'bedrooms': 4,
            'bathrooms': 3,
            'square_feet': 2200,
            'parking_spaces': 2,
            'year_built': 2019,
            'furnished': False,
            'featured': False,
            'agent': agents[0],
        },
        {
            'title': 'Luxury 2-Bedroom Apartment',
            'description': 'Premium shortlet apartment with hotel-like amenities and services.',
            'property_type': 'apartment',
            'listing_type': 'shortlet',
            'price': Decimal('45000'),
            'location': 'Victoria Island, Lagos',
            'state': 'lagos',
            'bedrooms': 2,
            'bathrooms': 2,
            'square_feet': 1200,
            'parking_spaces': 1,
            'year_built': 2021,
            'furnished': True,
            'featured': True,
            'min_stay_nights': 3,
            'wifi': True,
            'pool': True,
            'gym': True,
            'security': True,
            'air_conditioning': True,
            'agent': agents[4],
        },
        {
            'title': 'Executive 3-Bedroom Duplex',
            'description': 'Luxury shortlet duplex with modern amenities and 24/7 security.',
            'property_type': 'duplex',
            'listing_type': 'shortlet',
            'price': Decimal('65000'),
            'location': 'Lekki Phase 1, Lagos',
            'state': 'lagos',
            'bedrooms': 3,
            'bathrooms': 3,
            'square_feet': 1800,
            'parking_spaces': 2,
            'year_built': 2022,
            'furnished': True,
            'featured': False,
            'min_stay_nights': 2,
            'wifi': True,
            'generator': True,
            'security': True,
            'air_conditioning': True,
            'agent': agents[0],
        },
        {
            'title': 'Modern Family Home',
            'description': 'Beautiful family home in Abuja with spacious rooms and modern finishes.',
            'property_type': 'house',
            'listing_type': 'sale',
            'price': Decimal('75000000'),
            'location': 'Maitama, Abuja',
            'state': 'abuja',
            'bedrooms': 4,
            'bathrooms': 3,
            'square_feet': 2800,
            'parking_spaces': 2,
            'year_built': 2021,
            'furnished': False,
            'featured': True,
            'agent': agents[1],
        },
    ]
    
    for property_data in properties_data:
        property_obj, created = Property.objects.get_or_create(
            title=property_data['title'],
            defaults=property_data
        )
        if created:
            print(f"Created property: {property_obj.title}")
    
    print("Sample data creation completed!")

create_sample_data()
