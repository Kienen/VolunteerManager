# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Team describes a Department
class Team(models.Model):
    #Budget =  Number of team members allowed
    budget = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    visible = models.BooleanField(default= True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/team/%s" % (self.id)
        
    def get_available(self):
        return self.budget - Volunteer.objects.filter(team=self)

#The Volunteer class contains basic information about the Volunteer. OneToOneField relationship to the user.     
class Volunteer(models.Model):
    class Meta:
        ordering = ['first_name']
        
    #CONSTANTS
    DIET_CHOICES = (
        ('Omnivore', "Omnivore - I like everything including Meat"),
        ('Vegetarian', "Vegetarian - I don't eat any meat"),
        ('Vegan', "Vegan - I don't eat any animal products!"),
    )
    PUBLIC_FIELD_NAMES = [ 'first_name', 'last_name' , 'email', 'playa_name', 'birthdate', 'phone', 'emergency_contact', 'emergency_phone',
        'FB_user_name', 'diet', 'diet_restriction', 'disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'v_other', 'vexp_other', 'super_powers', 'jokes', 'ass']
    
    AVAILABILITY_FIELD_NAMES = ['avail_tu','avail_w' ,'avail_th', 'avail_f','avail_sa' ,'avail_su', 'avail_m']

    user = models.OneToOneField(User, related_name="profile", null=True)
    
    #User input fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    playa_name = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField('Birth Date', help_text="mm/dd/yyyy")
    phone = models.CharField(max_length=20, help_text="'999-999-9999'") 
    emergency_contact = models.CharField(max_length=30)
    emergency_phone = models.CharField(max_length=20, help_text="'999-999-999'") 
    FB_user_name = models.CharField('Facebook User Name', max_length=30, blank=True, help_text='(http://www.facebook.com/--->USER NAME<--)')
    diet = models.CharField('Dietary Preference', max_length=30, choices = DIET_CHOICES, default='Omnivore', help_text='Please choose the answer that *best* fits your dietary lifestyle.')
    diet_restriction = models.CharField('Specific dietary restriction', max_length=254, blank=True, 
                                        help_text="Please list any food allergies. We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs.")
    disability = models.CharField('Do you have any health or disability issues we should be aware of?', max_length=254, blank=True)
    attended_BM = models.BooleanField('Have you attended a Burning Man event before?', default=False)
    v_YOUtopia = models.BooleanField('Have you volunteered with YOUtopia before?', default=False)
    vexp_YOUtopia = models.CharField('If YES, which teams have you worked with?', max_length=254, blank=True)
    v_other = models.BooleanField('Have you volunteered with any other festivals or events before? ', default=False)
    vexp_other = models.CharField('If YES, please specify.', max_length=254, blank = True)
    super_powers = models.CharField('Super Powers', max_length=254, blank = True, help_text = "What special super powers or skills you have? What skills would you like to learn more about?")
    jokes = models.CharField('Questions? Comments? Favorite Joke?', max_length=254, blank = True, help_text="How do you kill a circus? Go for the juggler.")
    ass = models.BooleanField('Are you interested in taking on more responsibility than most volunteers to make your department run smoothly and YOUtopia better than ever?', default=False, blank=True,  help_text="Some teams will be choosing the most dedicated, experienced volunteers to train as assistants to the leads. These super volunteers will receive more training and more responsibility. Not everyone is cut out for this position, but we're looking for the best of the best.")
 
    #Availabiliity
    avail_tu = models.BooleanField('Tuesday, October 13th',default=True, blank=True)
    avail_w = models.BooleanField('Wednesday, October 14st', default=True, blank=True)
    avail_th = models.BooleanField('Thursday, October 15nd', default=True, blank=True)
    avail_f = models.BooleanField('Friday, October 16th', default=True, blank=True)
    avail_sa = models.BooleanField('Saturday, October 17th', default=True, blank=True)
    avail_su = models.BooleanField('Sunday, October 18th', default=True, blank=True)
    avail_m = models.BooleanField('Monday, October 19th', default=True, blank=True)
    
    #Team Choices
    approved = models.BooleanField('Have you already been selected to be part of a team?', default=False,  help_text="Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests.", blank= True)
    approved_by = models.CharField(max_length=30, blank=True)
    suggested_team = models.ForeignKey('Team', null=True, related_name = 'suggested_team', blank=True)
    team = models.ForeignKey('Team', blank= True, null=True, related_name='team')
    ratings = models.ManyToManyField(Team, through='Rating', related_name='ratings')
    
    #These fields are for administrative use.
    has_ticket = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)
    volunteer_rating = models.PositiveSmallIntegerField(null=True) 
    notes = models.CharField(max_length=254, blank=True) 
    limbo = models.BooleanField(default=False)
        
    #Methods
    def __str__(self):
        return self.first_name + " " + self.last_name
        
    def get_absolute_url(self):
        return  '/team/volunteers/' + str(self.id)


class Rating(models.Model):
    RATING_CHOICES = tuple((x, x) for x in range(1,6))
    volunteer = models.ForeignKey(Volunteer)
    team = models.ForeignKey(Team)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=1)
    
    def __str__(self):
        return self.team.name + ": " + str(self.rating)
    
