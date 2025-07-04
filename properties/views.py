from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Property, PropertyInquiry
from agents.models import Agent

def home(request):
    featured_properties = Property.objects.filter(featured=True, available=True)[:6]
    featured_agents = Agent.objects.filter(is_active=True)[:4]
    
    context = {
        'featured_properties': featured_properties,
        'featured_agents': featured_agents,
    }
    return render(request, 'properties/home.html', context)

def property_list(request, listing_type=None):
    properties = Property.objects.filter(available=True)
    
    if listing_type:
        properties = properties.filter(listing_type=listing_type)
    
    # Search and filtering
    search_query = request.GET.get('search')
    if search_query:
        properties = properties.filter(
            Q(title__icontains=search_query) | 
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    property_type = request.GET.get('property_type')
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    state = request.GET.get('state')
    if state:
        properties = properties.filter(state=state)
    
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)
    
    min_price = request.GET.get('min_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    
    max_price = request.GET.get('max_price')
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    furnished = request.GET.get('furnished')
    if furnished == 'true':
        properties = properties.filter(furnished=True)
    elif furnished == 'false':
        properties = properties.filter(furnished=False)
    
    # Sorting
    sort_by = request.GET.get('sort', 'featured')
    if sort_by == 'price_low':
        properties = properties.order_by('price')
    elif sort_by == 'price_high':
        properties = properties.order_by('-price')
    elif sort_by == 'newest':
        properties = properties.order_by('-created_at')
    elif sort_by == 'beds':
        properties = properties.order_by('-bedrooms')
    else:
        properties = properties.order_by('-featured', '-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get page title based on listing type
    page_titles = {
        'sale': 'Properties for Sale',
        'rent': 'Properties for Rent',
        'shortlet': 'Shortlet Properties'
    }
    page_title = page_titles.get(listing_type, 'All Properties')
    
    context = {
        'page_obj': page_obj,
        'listing_type': listing_type,
        'page_title': page_title,
        'property_types': Property.PROPERTY_TYPES,
        'states': Property.STATES,
        'current_filters': request.GET,
    }
    return render(request, 'properties/property_list.html', context)

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk, available=True)
    related_properties = Property.objects.filter(
        listing_type=property.listing_type,
        state=property.state,
        available=True
    ).exclude(pk=property.pk)[:3]

    # Get main image for this property
    main_image = property.images.filter(is_main=True).first()
    # If no main image, get any image
    if not main_image:
        main_image = property.images.first()

    if request.method == 'POST':
        inquiry = PropertyInquiry(
            property=property,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        inquiry.save()
        # Add success message here

    context = {
        'property': property,
        'main_image': main_image,
        'related_properties': related_properties,
    }
    return render(request, 'properties/property_detail.html', context)
