from django import forms
from Volunteer.models import *
from django.template.defaultfilters import mark_safe
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.formsets import formset_factory

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self])+'<br>')
            


class VolunteerNotesForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['notes']

class VolunteerForm(forms.ModelForm):
    diet_restriction = forms.CharField(max_length=30, label='Specific dietary restriction:',  required=False,
                                        help_text=mark_safe("Please list any food allergies. <br>We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs."))
    vexp_YOUtopia = forms.CharField(label=mark_safe('If so, which teams have you worked with?'), widget=forms.Textarea, required=False)
    vexp_other = forms.CharField(label=mark_safe('If so, please specify.'), widget=forms.Textarea, required=False)
    super_powers = forms.CharField(label=mark_safe('What special super powers or skills you have? What skills would you like to learn more about?'), widget=forms.Textarea, required=False)
    jokes = forms.CharField(label=mark_safe('Questions? Comments? Favorite Joke?'), widget=forms.Textarea, required=False, help_text="How do you kill a circus? Go for the juggler.")

    class Meta:
        model = Volunteer
        fields = Volunteer.PUBLIC_FIELD_NAMES + Volunteer.AVAILABILITY_FIELD_NAMES
        exclude = ['email']
        
        
class VolunteerSuggestForm(forms.ModelForm):
    #suggested_team = forms.ModelChoiceField(label="Suggested Team", required = False, queryset= Team.objects.all(), to_field_name="name")
    #notes = forms.CharField(max_length=30, label='Notes',  required=False)
    class Meta:
        model = Volunteer
        fields = [ 'first_name', 'last_name' ,  'playa_name', 'suggested_team', 'limbo', 'notes', 'birthdate',
                  'FB_user_name',  'disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 
                  'v_other', 'vexp_other', 'super_powers', 'jokes', 'ass'] + Volunteer.AVAILABILITY_FIELD_NAMES 
        
        
    
class ReadOnlyFieldsMixin(object):
    readonly_fields =()

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldsMixin, self).__init__(*args, **kwargs)
        for field in (field for name, field in self.fields.iteritems() if name in self.readonly_fields):
            field.widget.attrs['disabled'] = 'true'
            field.required = False
            
        for field in (field for name, field in self.fields.iteritems()):
            field.required = False

    def clean(self):
        cleaned_data = super(ReadOnlyFieldsMixin,self).clean()
        for field in self.readonly_fields:
           cleaned_data[field] = getattr(self.instance, field)

        return cleaned_data
        
class ReadOnlyVolunteerSuggestForm(ReadOnlyFieldsMixin, VolunteerSuggestForm):
    readonly_fields = Volunteer.PUBLIC_FIELD_NAMES + Volunteer.AVAILABILITY_FIELD_NAMES 
    


class RatingsForm(forms.Form):
    approved = forms.BooleanField(label='Are you a returning volunteer or have you already been selected to be part of a team?', 
                                  required = False, 
                                  help_text="Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests.")
    approved_team = forms.ModelChoiceField(label="Please select the team you've been recruited for", required = False, queryset= Team.objects.filter(visible=True), to_field_name="name")
    approved_by = forms.CharField(label='Which department head approved you?', max_length=30, required = False, help_text="Put (Returning) if you worked with this team last year.")
    
    def __init__(self, *args, **kwargs):
        teams = kwargs.pop('teams')
        super(RatingsForm, self).__init__()

        for team in teams:
            self.fields[team.name] = forms.ChoiceField(label=team.name, 
                                                                 help_text=team.description, 
                                                                 choices=tuple((x, x) for x in range(1,6)), 
                                                                 widget=forms.RadioSelect(renderer=HorizRadioRenderer))
RatingsFormSet= modelformset_factory

class VolunteerOfficeForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        exclude = ['user', 'ratings']
        
class ReadOnlyVolunteerForm (ReadOnlyFieldsMixin, VolunteerOfficeForm):
    readonly_fields = Volunteer.PUBLIC_FIELD_NAMES + Volunteer.AVAILABILITY_FIELD_NAMES 
    
#RatingsFormSet = inlineformset_factory(Team, Rating, extra=0)


    
'''
class SuggestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        volunteers = kwargs.pop('volunteers')
        super(SuggestForm, self).__init__()
        
        for volunteer in volunteers:
            self.fields[volunteer.id] = forms.ModelChoiceField(label=volunteer.first_name + volunteer.last_name,
                                                          queryset= Team.objects.all(), to_field_name="name",
                                                          required=False)
                                                          
'''                                                          