from .forms import AgentProfileForm
from agents.models import Agent
from django.contrib.auth.decorators import login_required
@login_required
def agent_profile_edit(request, user_id):
    # Only allow the agent to edit their own profile
    if request.user.id != user_id:
        return redirect('agent_dashboard')
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        return redirect('agent_dashboard')
    if request.method == 'POST':
        form = AgentProfileForm(request.POST, request.FILES, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agent_dashboard')
    else:
        form = AgentProfileForm(instance=agent)
    return render(request, 'accounts/agent_profile_form.html', {'form': form})
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from properties.models import Property

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on account type
            try:
                profile = user.userprofile
                if profile.account_type == 'agent':
                    return redirect('agent_dashboard')
                else:
                    return redirect('user_dashboard')
            except Exception:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        account_type = request.POST.get('account_type', 'user')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            from .models import UserProfile
            UserProfile.objects.create(user=user, account_type=account_type)
            # If registering as agent, create Agent instance as well
            if account_type == 'agent':
                from agents.models import Agent
                Agent.objects.create(user=user, company='', license_number=f'AGENT-{user.id}', phone='', email=email, location='', state='lagos', bio='', experience_years=0, specialties='', languages='')
            login(request, user)
            # Redirect based on account type after registration
            if account_type == 'agent':
                return redirect('agent_dashboard')
            else:
                return redirect('user_dashboard')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def user_dashboard(request):
    my_properties = Property.objects.filter(agent__user=request.user) if hasattr(request.user, 'agent') else []
    profile = None
    try:
        profile = request.user.userprofile
    except Exception:
        pass
    return render(request, 'accounts/user_dashboard.html', {'my_properties': my_properties, 'profile': profile})

@login_required
def agent_dashboard(request):
    try:
        profile = request.user.userprofile
    except Exception:
        return redirect('user_dashboard')
    if profile.account_type != 'agent':
        return redirect('user_dashboard')
    my_properties = Property.objects.filter(agent__user=request.user) if hasattr(request.user, 'agent') else []
    return render(request, 'accounts/agent_dashboard.html', {'my_properties': my_properties})
