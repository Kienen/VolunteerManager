# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect#, get_or_create
#from registration.backends.simple.views import RegistrationView
from Volunteer.models import *
from django.http import HttpResponse
#from django.views.generic.edit import CreateView, UpdateView
#from django.forms import ModelForm
from guardian.shortcuts import get_objects_for_user
#from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm
from django.contrib.auth.decorators import user_passes_test, permission_required
#from django.views.generic.list import ListView
#from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from Volunteer.forms import *

# Create your views here.
#def islead(user)
#    if useruser.groups.filter(name="leads").exists()

def volunteer_create(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        try:
            volunteer = Volunteer.objects.get(user=request.user)
            form = VolunteerForm(request.POST, instance=volunteer)
        except:
            form = VolunteerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
                profile =  form.save(commit=False)
                profile.user = request.user
                try:
                    profile.email = request.user.email
                except:
                    profile.email = "No Email Available"
                profile.save()
                # redirect to a new URL:
                if profile.approved:
                    redirect ('/home/')
                else:
                    return redirect('/ratings')
        else:
            
            return HttpResponse(request.POST.mew)
    # if a GET (or any other method) we'll create a blank form
    else:
        try:
            volunteer = Volunteer.objects.get(user=request.user)
            form= VolunteerForm(instance=volunteer)
        except:
            form = VolunteerForm(label_suffix='')

    return render(request, 'volunteer_form.html', {'form': list(form)})
 
def rating(request):
    teams = Team.objects.all()
    volunteer = request.user.profile
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RatingsForm(request.POST, teams= teams)
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            #preferences =  form.save(commit=False)
            #preferences.volunteer = request.user.profile
            #preferences.save()
        volunteer.ratings.clear()
        if request.POST.get('approved') == 'True':
            volunteer.suggested_team = preferences.approved_team
        else:
            for team in Team.objects.all():
                if request.POST.get(team.name):
                    r = Rating(volunteer= volunteer, team= team, rating=int(request.POST.get(team.name)))
                    r.save()
        volunteer.save()
        return  redirect('/home/')
 
    # if a GET (or any other method) we'll create a blank form
    else:

        form = RatingsForm(teams= teams)

    return render(request, 'rating_form.html', {
                                                'form': list(form),
                                                })        
    

def home(request):
    try:
        volunteer = request.user.profile
        return render(request, "home.html", {'volunteer' : volunteer} )
    except AttributeError: 
        return redirect(volunteer_create)



def go_profile(request):
    return redirect('/home/')
    
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")    
def team_choose(request):
    teams = get_objects_for_user(user=request.user, perms='Volunteer.change_team', klass=Team)
    return render(request, "team_choose.html", {'teams': teams})
    
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")
def team_view(request, team_arg):
    team_id = int(team_arg)
    try:
        this_team = Team.objects.get(id=team_id)
    except:
        return redirect('/team/')
    if not request.user.has_perm('Volunteer.change_team', this_team):  
        return redirect('/team/')
    
    approved_volunteer_list = Volunteer.objects.filter(team=this_team)
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.POST.get('Remove'):
            #volunteer = Volunteer database query SELECT id from website
            volunteer = Volunteer.objects.get(id=int(request.POST.get('Remove')))
            volunteer.team = None
            if volunteer.notes is None:
                volunteer.notes = "Removed from %s" % (this_team.name)
            else:
                volunteer.notes = volunteer.notes + " Removed from %s" % (this_team.name)
            volunteer.save()


        return redirect ('/team/%s' % (this_team.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        return render (request, "team_view.html",  {'this_team': this_team,
                                                    'approved_volunteer_list': approved_volunteer_list,
                                                    })

                                                    
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")
def suggest_view(request, team_arg):
    team_id = int(team_arg)
    try:
        this_team = Team.objects.get(id=team_id)
    except:
        return redirect('/team/')
    suggested_volunteer_list = Volunteer.objects.filter(suggested_team = this_team)
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        for volunteer in suggested_volunteer_list:
            if request.POST.get(str(volunteer.id)) == 'Accept':
                volunteer.team = this_team
                volunteer.suggested_team = None
            elif request.POST.get(str(volunteer.id)) == 'Reject':
                volunteer.suggested_team = None
                if volunteer.notes is None:
                    volunteer.notes = "Rejected by %s" % (this_team.name)
                else:
                    volunteer.notes = volunteer.notes + " Rejected by %s" % (this_team.name)
            volunteer.save()
        return redirect ('/team/%s/suggest' % (this_team.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        return render (request, "team_suggest.html",  {'this_team': this_team,
                                                    'suggested_volunteer_list': suggested_volunteer_list,
                                                    })
 
 
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")                                               
def unclaimed_view(request):
    VolunteerFormSet = modelformset_factory(Volunteer, form=ReadOnlyVolunteerSuggestForm, extra = 0)
    #volunteer_list = Volunteer.objects.all()#filter(team__isnull = True)
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        formset = VolunteerFormSet(request.POST)
        if formset.is_valid():
            print "saved"
            instances = formset.save()
            return redirect ('/team/volunteers/')
        else:
            print 'unsaved'
    # if a GET (or any other method) we'll create a blank form
    else:
        formset = VolunteerFormSet(queryset=Volunteer.objects.filter(team__isnull = True))
    return render (request, "suggest.html",  {'formset':formset
                                                    })
                                                    
                                                    
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")                                              
def email_view(request, team_arg):
    team_id = int(team_arg)
    try:
        this_team = Team.objects.get(id=team_id)
    except:
        return redirect('/team/')
    approved_volunteer_list = Volunteer.objects.filter(team=this_team)
    return render (request, "email_view.html",  {'this_team': this_team,
                                                'approved_volunteer_list': approved_volunteer_list,
                                                })
                                                
                                                
@user_passes_test(lambda u: u.groups.filter(name='leads').exists(), login_url="/team/login/")
def availability(request, team_arg):
    team_id = int(team_arg)
    try:
        this_team = Team.objects.get(id=team_id)
    except:
        return redirect('/team/')
    approved_volunteer_list = Volunteer.objects.filter(team=this_team)
    return render (request, "availability_view.html",  {'this_team': this_team,
                                                'approved_volunteer_list': approved_volunteer_list,
                                                })

                                                
@permission_required('Volunteer.add_team')                                            
def initialize(request):
    #from Volunteer.models import Team
    TEAMS = {'ADA': 5,
            'Center Camp': 5,
            'City Planning': 12,
            'Commissary': 35,
            'Dispatch': 5,
            'Dispensary': 8,
            'Fire': 13,
            'Gate': 32,
            'Greeters': 10,
            'Moopgicians': 23,
            'Outreach': 11,
            'Paparaunchy': 5,
            'Playshops': 11,
            'Please': 38,
            'Road Warriors': 44,
            'Sales': 5,
            'Swag': 5,
            'Teleportus': 38,
            'Ticketing': 16,
            'Waldos': 40,
            'Wolf Pack':22,
            }
            
    TEAM_DESCRIPTION_DICT = {
            'ADA': "Mobility Assistance",
            'Center Camp': "Whether it’s managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.",
            'City Planning': "Whether it's managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.",
            'Commissary': "So you're hungry, are you? The good people at the Commissary make sure the event crew can stay fat and sassy by keeping them fed, because we all love to keep it sassy.",
            'Dispatch': "Dispatch are the masters of radio communication. They keep our airwaves clear and help distribute information. Over.",
            'Dispensary': "I got what you want. I got what you need. The dispensary maintains YOUtopia supplies and equipment and makes sure each department is set up for success.",
            'Fire': "Keeping us safe from lighting ourselves, others, and anything other than approved art and performance on fire, Fire Safety knows to keep the fire alive at the event. They’re also the hard working crew that facilitates safety classes at the event to give you your first opportunity (or perhaps your 7,456,398 opportunity) to light up your fire.",
            'Gate': "These are the people who make sure your entrance into the event is a smooth ride. They check that you know about the rules concerning what you can bring into the event (No Glass or Firewood please!), make sure you have your ticket, and work closely with Security to protect the perimeter of the event.",
            'Greeters': "These are the folks that welcome participants with open arms into YOUtopia, while making sure you know where you’re going, providing answers to your questions about the event, and giving you a good hug (or a good spanking) at your request. ",
            'Moopgicians': "The Moopgician crew makes sure that participants leave a pristine location when the event is over. They help educate participants on having the least ecological impact and “Pack It In, Pack It Out” principles. They may also sometimes be found leading scavenger hunts and games.",
            'Outreach': "Masters of media relations and information dissemination, the OUTreach team knows what's shakin' and keeps the party rockin'.",
            'Paparaunchy': "If there's a totally righteous party in the forest, and no one is there to see it, did it really happen? Our media crew documents building the city from the early planning meetings to cleaning up on the way out.",
            'Playshops': "Aptly titled because they’re all about play!, Playshops provide activities like that early sunrise yoga to get a jumpstart to your day, a lesson on how to plant your very own unicorn, or a open dialogue about what it means to be a burner. Playshops & Performances Support play cupid, matchmaking Theme Camps with open space to host with those seeking a space to express their creativity. As wide-ranging as the imagination, they sometimes need a little support with those yoga mats or unicorn seeds.",
            'Please': "The Please Department supports the service of all other YOUtopia volunteer crews. They’re an elite strike force whose mission is to ensure members of the event team take care of themselves by delivering food, snacks, extra help, and overall fun. When not caretaking for other departments, they can usually be found instigating shenanigans somewhere in the event.",
            'Road Warriors': "The Road Warriors make sure we can all fit comfortably in the event. Working closely with City Planning, Road Warriors have a good handle on mapping out how exactly to fit all the cars, RVs, and other vehicles into the event with style and grace. They're looking for experienced volunteers who work hard and play hard.",
            'Sales': "Slinging coffee and ice on the mountain, the Sales crew wakes us up and keeps things cool, and donates the proceeds to the tribe.",
            'Swag': "Make 2015 memorable for all our volunteers with awesome gear and nifty collectibles.",
            'Teleportus': "Facilitating shuttles and art cars to help cruise participants around YOUtopia in style, TeleportUs crew keeps it movin.",
            'Ticketing': "They're making a list and checking it twice. These volunteers keep the line cruising.",
            'Waldos': "The Waldos keep an eagle eye open for uninvited guestss. They maintain a drag net to keep the perimeter secure and work closely with security to ensure anyone who isn't supposed to be at the event isn't at the event.",  
            'Wolf Pack': "Abiding by their motto, \"First To Come, Last To Pull Out,\" the Wolf Pack are a die hard crew. Literally building the event from the ground up, this crew sees to it that the infrastructure for our fair YOUtopian city is in place for the event. They are also responsible for disassembling everything at the conclusion of the event so our city leaves no trace.",
                          }
                          
    for team_name, budget in TEAMS.iteritems():
        
        (team, teamcreated) = Team.objects.get_or_create(budget= budget, name= team_name, description = TEAM_DESCRIPTION_DICT[team_name])
        this_name = team_name.replace(" ", "")
        this_name = this_name.lower()

        (newgroup,createdgroup) = Group.objects.get_or_create(name= this_name)
        try:
            (lead, createdlead) = User.objects.get_or_create(username= this_name)
        except:
            lead= User.objects.get(username= this_name)
        if createdlead:
            User.set_password("glitteringprizes")
        (leadgroup, leadgroupcreated) = Group.objects.get_or_create(name='leads')
        
        lead.save()
        newgroup.save()
        
        leadgroup.user_set.add(lead)
        leadgroup.save()
        newgroup.user_set.add(lead)
        
        assign_perm('change_team', newgroup, team)
        newgroup.save()
        
    leadgroup.user_set.add(User.objects.get(username='admin'))
    leadgroup.save()
    return HttpResponse('Initialize Successful!')
    



    

