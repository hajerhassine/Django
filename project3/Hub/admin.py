from dataclasses import fields
from django.contrib import admin
#from .models import *
# Register your models here.
from .models import User
from .models import Student
from .models import Coach
from .models import Project
from .models import MembershipInProjects

# relier la table student avec le projet 
#  StackedInline pour modifier l'affichage (verticale)
class ProjectInline(admin.StackedInline):
    model = Project
    # fieldsets = [
    #     (None,
    #      {
    #         'fields': ['project_name']
    #     }
    #     )
    # ]
class StudentAdmin(admin.ModelAdmin):
    list_display =(
        'FirstName',
        'LastName',
        'Email'
    )
    fields = (('FirstName','LastName'),
    'Email'
    )
    search_fields = ['LasteName']
    inlines= [
        ProjectInline,
    ]
    
@admin.register(Coach)    
class CoachAdmin(admin.ModelAdmin):
    list_display =(
        'FirstName',
        'LastName',
        'Email'
    )
    fields = (('FirstName','LastName'),
    'Email'
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        'project_name',
        'project_duration',
        'creator',
        'supervisor',
        
    )
    # fieldsets = [
    #     (None,
    #      {
    #         'fields': ['project_name','project_duration','creator','supervisor']
    #     }
    #     )
    # ]
    
    autocomplet_fields=['supervisor']
    fieldsets = [
        (
            'Etat',
         {
            'fields': ['isValid']
        }
        ),
         (
            'About',
         {
            'fields': ['project_name' ,'project_duration','creator','supervisor']
        }
        )
    ]
    
    # inverser l'ordre de projet
    # date_hierarchy='updated_at'

admin.site.register(User)
admin.site.register(Student , StudentAdmin)
#admin.site.register(Coach ,CoachAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(MembershipInProjects)

