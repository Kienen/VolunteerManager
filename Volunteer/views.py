from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from Volunteer.models import Volunteer
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.forms import ModelForm
from django import forms

# Create your views here.
def home(request):
#    volunteer = Volunteer.objects.get(id= request.user.id)
#    if volunteer is not None:
    if volunteer.is_active:
        info = {} 
        for field, value in volunteer:
            info[field] = value
        return render(request, "home.html", {'volunteer' : volunteer} )
    else:
        return HttpResponse("This account has been disabled. Please email Volunteer@sdyoutopia.com for more information.")

#class VolunteerRegistration(RegistrationView):
#    def get_success_url:
#        return "/home/"

def moo(request):
    vid = request.user.id
    return HttpResponse(vid)

class VolunteerForm(ModelForm):
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
'''    

#[
#        'playa_name' ,'birthdate' ,'phone' ,'emergency_contact' ,
#        'emergency_phone' ,   'FB_user_name' ,'diet' ,'diet_restriction','disability', 'attended_BM' ,'v_YOUtopia',
#        'vexp_YOUtopia' , 'v_other' , 'vexp_other', 'super_powers', 'jokes' ]
    
#UpdateVolunteerInfo allows the user to update their vital information.    
class UpdateVolunteer(UpdateView):
    #model = Volunteer
    #context_object_name = 'foo'
    #fields = Volunteer._meta.get_all_field_names()
    template_name = "volunteer_update_form.html"
    
    def get_object(self):
        return get_object_or_404(Volunteer, pk=self.request.user.id)
'''
def yah(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VolunteerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            profile =  form.save(commit=False)
            profile.user = request.user
            profile.save
            # redirect to a new URL:
            return HttpResponse('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VolunteerForm()

    return render(request, 'volunteer_form.html', {'form': form})
