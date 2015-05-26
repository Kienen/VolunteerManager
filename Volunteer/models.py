from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Team describes a Department
class Team(models.Model):
    #Budget =  Number of team members allowed
    budget = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)

    def __str__(self):
        return name

#The Volunteer class contains basic information about the Volunteer. OneToOneField relationship to the user.     
class Volunteer(models.Model):
    #CONSTANTS
    OMNIVORE = 1
    VEGETARIAN = 2
    VEGAN = 3
    DIET_CHOICES = (
        (OMNIVORE, 'Omnivore - I like everything including Meat'),
        (VEGETARIAN, 'Vegetarian - I don\'t eat any meat'),
        (VEGAN, 'Vegan - I don\t eat any animal products!'),
    )
    user = models.OneToOneField(User, related_name="profile")
    
    #User input fields
    #username = user.username
    #first_name = user.first_name
    #last_name = user.last_name
    #email = user.email
    playa_name = models.CharField(max_length=30, null=True)
    birthdate = models.DateTimeField('Birth Date')
    phone = models.CharField(max_length=20, help_text="'999-999-9999'") # validators should be a list
    emergency_contact = models.CharField(max_length=30)
    emergency_phone = models.CharField(max_length=20, help_text="'999-999-999'") # validators should be a list
    FB_user_name = models.CharField('Facebook User Name', max_length=30, null=True, help_text='(i.e. http://www.facebook.com/"YOU")')
    diet = models.IntegerField('Dietary Preference', choices = DIET_CHOICES, default=OMNIVORE, help_text='Please choose the answer that *best* fits your dietary lifestyle.')
    diet_restriction = models.CharField('Specific dietary restriction', max_length=254, null=True, help_text="Please list any food allergies. We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs.")
    disability = models.CharField('Do you have any health or disability issues we should be aware of?', max_length=254)
    attended_BM = models.BooleanField('Have you attended a Burning Man event before?', default=False)
    v_YOUtopia = models.BooleanField('Have you volunteered with YOUtopia before?', default=False)
    vexp_YOUtopia = models.CharField('If YES, which teams have you worked with?', max_length=254, null=True)
    v_other = models.BooleanField('Have you volunteered with any other festivals or events before? ', default=False)
    vexp_other = models.CharField('If YES, please specify.', max_length=254, null = True)
    super_powers = models.CharField('Super Powers', max_length=254, null = True, help_text = "What special super powers or skills you have? What skills would you like to learn more about?")
    jokes = models.CharField('Questions? Comments? Favorite Joke?', max_length=254, null = True, help_text="How do you kill a circus? Go for the juggler.")
    PUBLIC_FIELD_NAMES = [ 'playa_name', 'birthdate', 'phone', 'emergency_contact', 'emergency_phone',
        'FB_user_name', 'diet', 'diet_restriction', 'disability', 'attended_BM', 'v_YOUtopia', 'vexp_YOUtopia', 'super_powers', 'jokes']

    #These fields are for administrative use.
    suggested_team = models.CharField(max_length=30, null=True)
    team = models.ForeignKey('Team', null=True)
    has_ticket = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True) 
    notes = models.CharField(max_length=254, null=True)    
        
    #Methods
    def __str__(self):
        return self.first_name + " " + self.last_name
    def __iter__(self):
        for field_name in self.PUBLIC_FIELD_NAMES:
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)
            
#Preferences2015 describes a Volunteer's availability and 
#preferred teams in 2015. This has a One-to-One relationship with the Volunteer class.
class Preferences2015(models.Model):
    volunteer = models.OneToOneField(Volunteer)
    avail_tu = models.BooleanField(default=True)
    avail_w = models.BooleanField(default=True)
    avail_th = models.BooleanField(default=True)
    avail_f = models.BooleanField(default=True)
    avail_sa = models.BooleanField(default=True)
    avail_su = models.BooleanField(default=True)
    avail_m = models.BooleanField(default=True)
    ass = models.BooleanField(default=False)
    team_preferences = {}
    def __iter__(self):
        for field_name in self._meta.get_all_field_names():
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)
