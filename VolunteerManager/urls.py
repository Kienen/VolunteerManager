from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends import simple
from Volunteer import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required 

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/register/complete/$', views.volunteer_create), 
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^home/$', login_required(views.home)),

    #Profiles
    url(r'^profile/$', login_required(views.volunteer_create)),
    url(r'^profile/2015/$', login_required(views.preferences2015_create)),

    
    #Password setting urls with built-in templates
    url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset, name='auth_password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
)
