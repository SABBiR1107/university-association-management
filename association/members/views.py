from django.shortcuts import render
from django.http import HttpResponse
from .models import Division, Position, Member

def index(request):
    divisions = Division.objects.all()
    core_positions = Position.objects.filter(division__name__icontains='core', hierarchy_order__gte=0).order_by('hierarchy_order')
    core_members = Member.objects.filter(position__in=core_positions, is_active=True)
    
    context = {
        'divisions': divisions,
        'core_members': core_members,
    }
    return render(request, 'index.html', context)

def members_list(request):
    divisions = Division.objects.prefetch_related('positions__members').all()
    
    context = {
        'divisions': divisions,
    }
    return render(request, 'members.html', context)

def contact(request):
    return render(request, 'contact.html')