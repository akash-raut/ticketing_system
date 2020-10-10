from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    ''' Includes extra fields to display in admin page and add extra properties '''
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']


admin.site.register(Project, ProjectAdmin)


