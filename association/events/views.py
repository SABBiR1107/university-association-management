from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone

def events_list(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now(), is_active=True)
    past_events = Event.objects.filter(date__lt=timezone.now(), is_active=True)
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'events.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id, is_active=True)
    context = {
        'event': event,
    }
    return render(request, 'event_detail.html', context)