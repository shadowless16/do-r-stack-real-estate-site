from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('duplex', 'Duplex'),
        ('terrace', 'Terrace'),
        ('penthouse', 'Penthouse'),
        ('studio', 'Studio'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
    ]
    
    LISTING_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('shortlet', 'Shortlet'),
    ]
    
    STATES = [
        ('lagos', 'Lagos'),
        ('abuja', 'Abuja'),
        ('kano', 'Kano'),
        ('port-harcourt', 'Port Harcourt'),
        ('ibadan', 'Ibadan'),
        ('kaduna', 'Kaduna'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=STATES)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    square_feet = models.PositiveIntegerField()
    parking_spaces = models.PositiveIntegerField(default=0)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    furnished = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    min_stay_nights = models.PositiveIntegerField(null=True, blank=True, help_text="For shortlets only")
    
    # Amenities for shortlets
    wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    generator = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    
    agent = models.ForeignKey('agents.Agent', on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'pk': self.pk})

    def get_price_display(self):
        if self.listing_type == 'rent':
            return f"₦{self.price:,.0f}/year"
        elif self.listing_type == 'shortlet':
            return f"₦{self.price:,.0f}/night"
        else:
            return f"₦{self.price:,.0f}"

    def get_amenities(self):
        amenities = []
        if self.wifi: amenities.append('WiFi')
        if self.pool: amenities.append('Pool')
        if self.gym: amenities.append('Gym')
        if self.security: amenities.append('Security')
        if self.generator: amenities.append('Generator')
        if self.kitchen: amenities.append('Kitchen')
        if self.air_conditioning: amenities.append('AC')
        return amenities


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_main', 'created_at']

    def __str__(self):
        return f"{self.property.title} - Image"


class PropertyInquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Property Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry for {self.property.title} by {self.name}"
