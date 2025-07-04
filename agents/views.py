from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Agent

def agent_list(request):
    agents = Agent.objects.filter(is_active=True)
    
    # Search and filtering
    search_query = request.GET.get('search')
    if search_query:
        agents = agents.filter(
            Q(user__first_name__icontains=search_query) | 
            Q(user__last_name__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(specialties__icontains=search_query)
        )
    
    agent_type = request.GET.get('agent_type')
    if agent_type:
        agents = agents.filter(agent_type=agent_type)
    
    state = request.GET.get('state')
    if state:
        agents = agents.filter(state=state)
    
    min_experience = request.GET.get('min_experience')
    if min_experience:
        agents = agents.filter(experience_years__gte=min_experience)
    
    min_rating = request.GET.get('min_rating')
    if min_rating:
        agents = agents.filter(rating__gte=min_rating)
    
    # Sorting
    sort_by = request.GET.get('sort', 'rating')
    if sort_by == 'rating':
        agents = agents.order_by('-rating', '-total_reviews')
    elif sort_by == 'experience':
        agents = agents.order_by('-experience_years')
    elif sort_by == 'properties':
        agents = agents.order_by('-properties__count')
    elif sort_by == 'reviews':
        agents = agents.order_by('-total_reviews')
    else:
        agents = agents.order_by('-is_featured', '-rating')
    
    # Pagination
    paginator = Paginator(agents, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'agent_types': Agent.AGENT_TYPES,
        'states': Agent.STATES,
        'current_filters': request.GET,
    }
    return render(request, 'agents/agent_list.html', context)

def agent_detail(request, pk):
    agent = get_object_or_404(Agent, pk=pk, is_active=True)
    agent_properties = agent.properties.filter(available=True)[:6]
    
    context = {
        'agent': agent,
        'agent_properties': agent_properties,
    }
    return render(request, 'agents/agent_detail.html', context)
