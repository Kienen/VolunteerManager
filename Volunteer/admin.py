from django.contrib import admin
from Volunteer.models import Volunteer, Team, Preferences2015

# Register your models here.
class AvailabilityInline(admin.TabularInline):
    model = Preferences2015
    readonly_fields = ['avail_tu','avail_w' ,'avail_th', 'avail_f','avail_sa' ,'avail_su', 'avail_m']
    fieldsets = [
        ('Availability', {'fields': ['avail_tu','avail_w' ,'avail_th', 'avail_f','avail_sa' ,'avail_su', 'avail_m']})

        ]
        
class TeamInline(admin.TabularInline):
    model = Preferences2015
    verbose_name = "Team Preferences"
    readonly_fields = ['ada','art_curation','center_camp','city_planning','commissary','dispatch','dispensary','fire','gate','greeters','lnt','outreach','paparaunchy','playshops','please','road_warriors','sales','swag','teleportus' ,'ticketing' ,'waldos','wolf_pack']
    fieldsets = [

        ('Team', {'fields': ['ada','art_curation','center_camp','city_planning','commissary','dispatch','dispensary','fire','gate','greeters','lnt','outreach','paparaunchy','playshops','please','road_warriors','sales','swag','teleportus' ,'ticketing' ,'waldos','wolf_pack']})
        ]

 
class VolunteerAdmin(admin.ModelAdmin):
        readonly_fields = ['first_name','last_name',  'disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'v_other', 'vexp_other','super_powers','jokes']
        fieldsets = [
            (None,  {'fields': ['first_name','last_name', 'team', 'suggested_team', 'notes']}),
            ('Information', {'fields': ['disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'v_other', 'vexp_other','super_powers','jokes'], 'classes': ['collapse']})
            ]
        
        inlines = [AvailabilityInline, TeamInline]
        list_filter = ['suggested_team', 'team']
        
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Team)
#admin.site.register(Preferences2015)