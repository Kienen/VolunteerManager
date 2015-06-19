from django.shortcuts import render, redirect
#from registration.backends.simple.views import RegistrationView
from Volunteer.models import *
from django.http import HttpResponse
#from django.views.generic.edit import CreateView, UpdateView
#from django.forms import ModelForm


#from django.views.generic.list import ListView
#from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from Volunteer.forms import *

# Create your views here.


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
                return redirect('/profile/team/')
 
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
    
def team_choose(request):
        return render(request, "team_choose.html", {'teams': Team.objects.all()})
    

def team_view(request, team_arg):
    team_id = int(team_arg)
    try:
        this_team = Team.objects.get(id=team_id)
    except:
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




    

