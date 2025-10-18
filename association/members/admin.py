from django.contrib import admin
from .models import Division, Position, Member

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority', 'description']
    list_editable = ['priority']
    search_fields = ['name']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'division', 'hierarchy_order']
    list_editable = ['hierarchy_order']
    list_filter = ['division']
    search_fields = ['name']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'display_order', 'email', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['position__division', 'is_active']
    search_fields = ['name', 'position__name']