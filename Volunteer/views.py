from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from Volunteer.models import Volunteer
from django.http import HttpResponse
#from django.views.generic.edit import CreateView, UpdateView
#from django.forms import ModelForm
from django import forms
from django.template.defaultfilters import mark_safe

# Create your views here.
class VolunteerForm(forms.ModelForm):
    #playa_name = forms.CharField(max_length=30, required=False)
    diet_restriction = forms.CharField(max_length=30, label='Specific dietary restriction',  required=False,
                                        help_text=mark_safe("Please list any food allergies. <br>We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs."))
    #disability = forms.CharField(label='Do you have any health or disability issues we should be aware of?', max_length=30, required=False)
    vexp_YOUtopia = forms.CharField(label=mark_safe('If YES, which teams have you worked with?<br>'), widget=forms.Textarea, required=False)
    vexp_other = forms.CharField(label=mark_safe('If YES, please specify.<br>'), widget=forms.Textarea, required=False)
    super_powers = forms.CharField(label=mark_safe('Super Powers<br>'), widget=forms.Textarea, required=False)
    jokes = forms.CharField(label=mark_safe('Questions? Comments? Favorite Joke?<br>'), widget=forms.Textarea, required=False)

    class Meta:
        model = Volunteer
        fields = Volunteer.PUBLIC_FIELD_NAMES

class Preferences2015Form(forms.ModelForm):
    class Meta:
        model = Preferences2015
        fields = ['__all__']
        exclude = ['user']


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
            profile.save()
            # redirect to a new URL:
            return redirect('/profile/2015')
 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VolunteerForm()

    return render(request, 'volunteer_form.html', {'form': form})

def preferences2015_create(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Preferences2015Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            profile =  form.save(commit=False)
            profile.user = request.user
            profile.save()
            # redirect to a new URL:
            return redirect('/home/')
 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Preferences2015Form()

    return render(request, 'volunteer_form.html', {'form': form})

def home(request):
    try:
        volunteer = request.user.profile
        return render(request, "home.html", {'volunteer' : volunteer} )
    except AttributeError: 
        return redirect(volunteer_create)



def go_profile(request):
    return redirect('/home/')

