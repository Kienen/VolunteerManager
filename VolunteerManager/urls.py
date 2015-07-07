from django.conf.urls import patterns, include, url
from django.contrib import admin
from Volunteer import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required 
from registration.backends import simple

urlpatterns = patterns('',
    url(r'^', include('favicon.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^initialize/', views.initialize),
    #url(r'^passupdate/', views.passwordmassupdate),
    
    #Team Leads
    url(r'^team/$', views.team_choose),
    url(r'^team/(?P<team_arg>\d{1,})/$', views.team_view),
    url(r'^team/(?P<team_arg>\d{1,})/suggest$', views.suggest_view),
    url(r'^team/(?P<team_arg>\d{1,})/email$', views.email_view),
    url(r'^team/volunteers/$', views.unclaimed_list),
    url(r'^team/volunteers/(?P<vol_arg>\d{1,})/$', views.volunteer_detail_view, name='volunteer_detail'),
    url(r'^team/login/$', 'django.contrib.auth.views.login', { 'template_name': 'team_login.html'}),
    url(r'^team/(?P<team_arg>\d{1,})/availability$', views.availability),
    
 
    
    #Volunteer Profiles
    url(r'^home/$', login_required(views.home)),
    url(r'^profile/$', login_required(views.volunteer_create)),
    url(r'^ratings/$', login_required(views.rating)),
    url(r'^password/$', auth_views.password_change),
    

    #Registration
    url(r'^accounts/register/complete/$', views.volunteer_create),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'django.contrib.auth.views.login',  {'template_name': 'Volunteer/registration/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),


    #Password setting urls with built-in templates
    url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    #url(r'^password/reset/$', auth_views.password_reset, name='auth_password_reset'),
    #url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='auth_password_reset_confirm'),
    #url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
)
