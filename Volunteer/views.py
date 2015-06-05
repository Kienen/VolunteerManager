from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from Volunteer.models import Volunteer
from django.http import HttpResponse
#from django.views.generic.edit import CreateView, UpdateView
#from django.forms import ModelForm
from django import forms

# Create your views here.
def home(request):
    try:
        volunteer = request.user.profile
        return render(request, "home.html", {'volunteer' : volunteer} )
    except request.user.RelatedObjectDoesNotExist: 
        views.volunteer_create


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = Volunteer.PUBLIC_FIELD_NAMES
    playa_name = forms.CharField(max_length=30, required=False)
    diet_restriction = forms.CharField(max_length=30, required=False)
    disability = forms.CharField(max_length=30, required=False)
    vexp_YOUtopia = forms.CharField(widget=forms.Textarea, required=False)
    vxp_other = forms.CharField(widget=forms.Textarea, required=False)
    super_powers = forms.CharField(widget=forms.Textarea, required=False)
    jokes = forms.CharField(widget=forms.Textarea, required=False)

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
            return redirect('/home/')
 #           return HttpResponse('Success! We will contact you after performing complex calculation, please join us in the YOUtopia Volunteers Facebook group!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VolunteerForm()

    return render(request, 'volunteer_form.html', {'form': form})

def go_profile(request):
    return redirect('/home/')