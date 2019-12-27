from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Details',
         {'fields': ['Middle_Name', 'First_Name','Last_Name','Type','Password' ]}),
        ('Contact Information', {'fields': ['Email', 'Phone_Number']}),

    ]
    list_display = ('Middle_Name', 'First_Name','Email')
    list_filter = ['Middle_Name', 'First_Name','Email']
    search_fields = ['Middle_Name', 'First_Name','Email']


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team Details',
         {'fields': ['TID', 'DID', 'Position', ]}),

    ]
    list_display = ('TID', 'DID')
    list_filter = ['TID', 'DID']
    search_fields = ['TID', 'DID']


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Details',
         {'fields': ['PID', 'TID', 'Title', ]}),

    ]
    list_display = ('PID', 'TID', 'Title',)
    list_filter = ['PID', 'TID', 'Title', ]
    search_fields = ['PID', 'TID', 'Title', ]


class ComplaintsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Complaints Details',
         {'fields': ['CID', 'UID', 'Complaint', ]}),

    ]
    list_display = ('CID', 'UID', 'Complaint',)
    list_filter = ['CID', 'UID', 'Complaint']
    search_fields = ['CID', 'UID', 'Complaint']


class Project_StatusAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project_Status Details',
         {'fields': ['PID', 'Status', ]}),

    ]
    list_display = ('PID', 'Status',)
    list_filter = ['PID', 'Status', ]
    search_fields = ['PID', 'Status', ]


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Complaints, ComplaintsAdmin)
admin.site.register(Project_Status, Project_StatusAdmin)
