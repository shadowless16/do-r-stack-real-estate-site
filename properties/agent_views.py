from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Property
from .forms import PropertyForm
from agents.models import Agent

@login_required
def property_create(request):
    # Only allow agents to create properties
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        return HttpResponseForbidden("You must be an agent to create a property.")

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = agent
            property.save()
            # Handle main image upload
            main_image = form.cleaned_data.get('main_image')
            if main_image:
                from .models import PropertyImage
                PropertyImage.objects.create(property=property, image=main_image, is_main=True)
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form, 'action': 'Create'})

@login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        return HttpResponseForbidden("You must be an agent to edit a property.")
    if property.agent != agent:
        return HttpResponseForbidden("You do not have permission to edit this property.")

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            property = form.save()
            # Handle main image upload (replace or add if provided)
            main_image = form.cleaned_data.get('main_image')
            if main_image:
                from .models import PropertyImage
                # Remove previous main image if exists
                PropertyImage.objects.filter(property=property, is_main=True).delete()
                PropertyImage.objects.create(property=property, image=main_image, is_main=True)
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_form.html', {'form': form, 'action': 'Edit'})

@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        return HttpResponseForbidden("You must be an agent to delete a property.")
    if property.agent != agent:
        return HttpResponseForbidden("You do not have permission to delete this property.")

    if request.method == 'POST':
        property.delete()
        return redirect('agent_dashboard')
    return render(request, 'properties/property_confirm_delete.html', {'property': property})
