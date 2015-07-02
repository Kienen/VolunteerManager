from django.contrib import admin
from Volunteer.models import Volunteer, Team, Rating
from guardian.admin import GuardedModelAdmin
# Register your models here.

       
class RatingInline(admin.TabularInline):
    model = Rating
    #verbose_name = "Team Preferences"
    readonly_fields = ['team', 'rating']
    fields = ['team', 'rating']
    extra = 0
    #filter_horizontal = ('team',)

class TeamAdmin(GuardedModelAdmin):
    fields = ['budget', 'name', 'description', 'visibile']
    
class VolunteerAdmin(admin.ModelAdmin):
        readonly_fields = ['first_name','last_name',  'disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'v_other', 'vexp_other','super_powers','jokes','ratings']
        fieldsets = [
            (None,  {'fields': ['first_name','last_name', 'team', 'suggested_team', 'notes']}),
            ('Information', {'fields': ['disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'v_other', 'vexp_other','super_powers','jokes'], 'classes': ['collapse']}),
            ('Availability', {'fields': ['avail_tu','avail_w' ,'avail_th', 'avail_f','avail_sa' ,'avail_su', 'avail_m'], 'classes': ['collapse']}),
            ]

        inlines = [RatingInline]
        list_filter = ['suggested_team', 'team']
        
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Team, TeamAdmin)
#admin.site.register(Preferences2015)