from django.shortcuts import render, redirect
#from registration.backends.simple.views import RegistrationView
from Volunteer.models import Volunteer, Preferences2015, Team
from django.http import HttpResponse
#from django.views.generic.edit import CreateView, UpdateView
#from django.forms import ModelForm
from django import forms
from django.template.defaultfilters import mark_safe
from django.views.generic.list import ListView

# Create your views here.
class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class VolunteerNotesForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['notes']

class VolunteerForm(forms.ModelForm):
    diet_restriction = forms.CharField(max_length=30, label='Specific dietary restriction:',  required=False,
                                        help_text=mark_safe("Please list any food allergies. <br>We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs."))
    vexp_YOUtopia = forms.CharField(label=mark_safe('<p>If so, which teams have you worked with?</p>'), widget=forms.Textarea, required=False)
    vexp_other = forms.CharField(label=mark_safe('<p>If so, please specify.</p>'), widget=forms.Textarea, required=False)
    super_powers = forms.CharField(label=mark_safe('What special super powers or skills you have? What skills would you like to learn more about?<p></p>'), widget=forms.Textarea, required=False)
    jokes = forms.CharField(label=mark_safe('Questions? Comments? Favorite Joke?<p></p>'), widget=forms.Textarea, required=False)

    class Meta:
        model = Volunteer
        fields = Volunteer.PUBLIC_FIELD_NAMES
        exclude = ['email']

class Preferences2015Form(forms.ModelForm):
    class Meta:
        model = Preferences2015
        fields = '__all__'
        exclude = ['volunteer']
        widgets = {
                    'ada': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'art_curation': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'center_camp': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'city_planning': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'commissary': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'dispatch': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'dispensary': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'fire': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'gate': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'greeters': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'lnt': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'outreach': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'paparaunchy': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'playshops': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'please': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'road_warriors': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'sales': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'swag': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'teleportus' : forms.RadioSelect(renderer=HorizRadioRenderer),
                    'ticketing' : forms.RadioSelect(renderer=HorizRadioRenderer),
                    'waldos': forms.RadioSelect(renderer=HorizRadioRenderer),
                    'wolf_pack': forms.RadioSelect(renderer=HorizRadioRenderer),
                    }
                    
        
        
     
    #availability = fields
    #availability = ['avail_tu', 'avail_w','avail_th','avail_f','avail_sa', 'avail_su','avail_m']
    teams_prefs = [
    'ada',
    'art_curation',
    'center_camp',
    'city_planning',
    'commissary',
    'dispatch',
    'dispensary',
    'fire',
    'gate',
    'greeters',
    'lnt',
    'outreach',
    'paparaunchy',
    'playshops',
    'please',
    'road_warriors',
    'sales',
    'swag',
    'teleportus' ,
    'ticketing' ,
    'waldos',
    'wolf_pack']

class CoordinatorView(ListView):
    model = Volunteer

def volunteer_create(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
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
            return redirect('/profile/2015')
 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VolunteerForm(label_suffix='')

    return render(request, 'volunteer_form.html', {'form': form})

def preferences2015_create(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Preferences2015Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            preferences =  form.save(commit=False)
            preferences.volunteer = request.user.profile
            if preferences.approved_team is not None:
                preferences.volunteer.suggested_team = preferences.approved_team
                preferences.volunteer.save()
            preferences.save()
            # redirect to a new URL:
            return redirect('/home/')
 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Preferences2015Form(label_suffix='')

    return render(request, 'preferences2015_form.html', {'form': list(form)})

def home(request):
    try:
        volunteer = request.user.profile
        preferences = request.user.profile.preferences2015
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
'''                                                    
def unclaimed_view(request, team_arg):
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
'''                                                    
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




    
    '''list of teams for easy cut/paste
    ada
    art_curation
    center_camp
    city_planning
    commissary
    dispatch
    dispensary
    fire
    gate
    greeters
    lnt
    outreach
    paparaunchy
    playshops
    please
    road_warriors
    sales
    swag
    teleportus 
    ticketing 
    waldos
    wolf_pack
    '''    
