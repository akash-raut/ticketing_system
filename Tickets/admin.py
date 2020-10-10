from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    ''' Includes extra fields to display in admin page and add extra properties '''
    list_display = ['id', 'name', 'assigned_to', 'status']
    list_display_links = ['id', 'name', 'assigned_to', 'status']
    search_fields = ['name', 'assigned_to']
    ordering = ['id']


admin.site.register(Ticket, TicketAdmin)


