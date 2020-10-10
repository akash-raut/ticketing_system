from django.contrib import admin

from .models import Staff_User


class StaffUserAdmin(admin.ModelAdmin):
    ''' Includes extra fields to display in admin page and add extra properties '''
    list_display = ['id', 'name', 'email', 'project_assigned', 'is_active']
    list_display_links = ['id', 'name', 'email']
    search_fields = ['name', 'email']
    ordering = ['id']


admin.site.register(Staff_User, StaffUserAdmin)
