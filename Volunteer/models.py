# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Team describes a Department
class Team(models.Model):
    #Budget =  Number of team members allowed
    budget = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return "/team/%s" % (self.id)
        
    def get_available(self):
        return self.budget - Volunteer.objects.filter(team=self)

#The Volunteer class contains basic information about the Volunteer. OneToOneField relationship to the user.     
class Volunteer(models.Model):
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
    email = models.CharField(max_length=30)
    playa_name = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField('Birth Date', help_text="mm/dd/yyyy")
    phone = models.CharField(max_length=20, help_text="'999-999-9999'") 
    emergency_contact = models.CharField(max_length=30)
    emergency_phone = models.CharField(max_length=20, help_text="'999-999-999'") 
    FB_user_name = models.CharField('Facebook User Name', max_length=30, blank=True, help_text='(i.e. http://www.facebook.com/"YOU")')
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
    #approved_team = models.ForeignKey('Team', null=True, blank=True)
    approved_by = models.CharField(max_length=30, blank=True)
    suggested_team = models.ForeignKey('Team', null=True, related_name = 'suggested_team', blank=True)
    team = models.ForeignKey('Team', blank= True, null=True, related_name='team')
    ratings = models.ManyToManyField(Team, through='Rating', related_name='ratings')
    
    #These fields are for administrative use.
    has_ticket = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)
    volunteer_rating = models.PositiveSmallIntegerField(null=True) 
    notes = models.CharField(max_length=254, null=True)    
        
    #Methods
    def __str__(self):
        return self.first_name + " " + self.last_name


class Rating(models.Model):
    RATING_CHOICES = tuple((x, x) for x in range(1,6))
    volunteer = models.ForeignKey(Volunteer)
    team = models.ForeignKey(Team)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=1)
    
    def __str__(self):
        return self.volunteer.first_name + " " + self.volunteer.last_name + " " +self.team.name + " " + str(self.rating)
    
''' 
#Preferences2015 describes a Volunteer's availability and 
#preferred teams in 2015. This has a One-to-One relationship with the User class.
class Preferences2015(models.Model):
    #CONSTANTS
    TEAM_DESCRIPTION_DICT = {
                      'ada': "Mobility Assistance",
                      'art_curation': "Coordinating with local artists to keep YOUtopia weird.",
                      'city_planning': "Whether it's managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.",
                      'center_camp': "Whether it’s managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.",
                      'commissary' : "So you're hungry, are you? The good people at the Commissary make sure the event crew can stay fat and sassy by keeping them fed, because we all love to keep it sassy.",
                      'dispatch' : "Dispatch are the masters of radio communication. They keep our airwaves clear and help distribute information. Over.",
                      'dispensary' : "I got what you want. I got what you need. The dispensary maintains YOUtopia supplies and equipment and makes sure each department is set up for success.",
                      'fire' : "Keeping us safe from lighting ourselves, others, and anything other than approved art and performance on fire, Fire Safety knows to keep the fire alive at the event. They’re also the hard working crew that facilitates safety classes at the event to give you your first opportunity (or perhaps your 7,456,398 opportunity) to light up your fire.",
                      'gate' : "These are the people who make sure your entrance into the event is a smooth ride. They check that you know about the rules concerning what you can bring into the event (No Glass or Firewood please!), make sure you have your ticket, and work closely with Security to protect the perimeter of the event.",
                      'greeters' : "These are the folks that welcome participants with open arms into YOUtopia, while making sure you know where you’re going, providing answers to your questions about the event, and giving you a good hug (or a good spanking) at your request. ",
                      'lnt' : "The Moopgician crew makes sure that participants leave a pristine location when the event is over. They help educate participants on having the least ecological impact and “Pack It In, Pack It Out” principles. They may also sometimes be found leading scavenger hunts and games.",
                      'outreach' : "Masters of media relations and information dissemination, the OUTreach team knows what's shakin' and keeps the party rockin'.",
                      'paparaunchy' : "If there's a totally righteous party in the forest, and no one is there to see it, did it really happen? Our media crew documents building the city from the early planning meetings to cleaning up on the way out.",
                      'playshops' : "Aptly titled because they’re all about play!, Playshops provide activities like that early sunrise yoga to get a jumpstart to your day, a lesson on how to plant your very own unicorn, or a open dialogue about what it means to be a burner. Playshops & Performances Support play cupid, matchmaking Theme Camps with open space to host with those seeking a space to express their creativity. As wide-ranging as the imagination, they sometimes need a little support with those yoga mats or unicorn seeds.",
                      'please' : "The Please Department supports the service of all other YOUtopia volunteer crews. They’re an elite strike force whose mission is to ensure members of the event team take care of themselves by delivering food, snacks, extra help, and overall fun. When not caretaking for other departments, they can usually be found instigating shenanigans somewhere in the event.",
                      'road_warriors' : "The Road Warriors make sure we can all fit comfortably in the event. Working closely with City Planning, Road Warriors have a good handle on mapping out how exactly to fit all the cars, RVs, and other vehicles into the event with style and grace. They're looking for experienced volunteers who work hard and play hard.",
                      'sales' : "Slinging coffee and ice on the mountain, the Sales crew wakes us up and keeps things cool, and donates the proceeds to the tribe.",
                      'swag' : "Make 2015 memorable for all our volunteers with awesome gear and nifty collectibles.",
                      'teleportus' : "Facilitating shuttles and art cars to help cruise participants around YOUtopia in style, TeleportUs crew keeps it movin.",
                      'ticketing' : "They're making a list and checking it twice. These volunteers keep the line cruising.",
                      'waldos' : "The Waldos keep an eagle eye open for uninvited guestss. They maintain a drag net to keep the perimeter secure and work closely with security to ensure anyone who isn't supposed to be at the event isn't at the event.",  
                      'wolf_pack' : "Abiding by their motto, \"First To Come, Last To Pull Out,\" the Wolf Pack are a die hard crew. Literally building the event from the ground up, this crew sees to it that the infrastructure for our fair YOUtopian city is in place for the event. They are also responsible for disassembling everything at the conclusion of the event so our city leaves no trace.",
                      'ass' : "Some teams will be choosing the most dedicated, experienced volunteers to train as assistants to the leads. These super volunteers will receive more training and more responsibility. Not everyone is cut out for this position, but we're looking for the best of the best.",
                      'team' : "Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests.",
                      }
                      
    RATING_CHOICES = tuple((x, x) for x in range(1,6))
    volunteer = models.OneToOneField(Volunteer, null=True)
    
    #availability
    avail_tu = models.BooleanField('Tuesday, October 13th',default=True, blank=True)
    avail_w = models.BooleanField('Wednesday, October 14st', default=True, blank=True)
    avail_th = models.BooleanField('Thursday, October 15nd', default=True, blank=True)
    avail_f = models.BooleanField('Friday, October 16th', default=True, blank=True)
    avail_sa = models.BooleanField('Saturday, October 17th', default=True, blank=True)
    avail_su = models.BooleanField('Sunday, October 18th', default=True, blank=True)
    avail_m = models.BooleanField('Monday, October 19th', default=True, blank=True)
    ass = models.BooleanField('Are you interested in taking on more responsibility than most volunteers to make your department run smoothly and YOUtopia better than ever?', default=False, blank=True,  help_text=TEAM_DESCRIPTION_DICT['ass'])

    #Team Choices
    approved = models.BooleanField('Have you already been selected to be part of a team?', default=False,  help_text=TEAM_DESCRIPTION_DICT['team'], blank= True)
    approved_team = models.ForeignKey('Team', null=True, blank=True)
    approved_by = models.CharField(max_length=30, blank=True)

    ratings = models.ManyToManyField(Team, through='Rating', related_name='ratings')
       
    ada= models.PositiveSmallIntegerField('ADA', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['ada'], default=1)
    art_curation = models.PositiveSmallIntegerField('Art Curation', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['art_curation'], default=1)
    center_camp = models.PositiveSmallIntegerField('Center Camp',null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['center_camp'], default=1)
    city_planning = models.PositiveSmallIntegerField('City Planning', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['city_planning'], default=1)
    commissary = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['commissary'], default=1)
    dispatch = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['dispatch'], default=1)
    dispensary = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['dispensary'], default=1)
    fire = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['fire'], default=1)
    gate = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['gate'], default=1)
    greeters = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['greeters'], default=1)
    lnt = models.PositiveSmallIntegerField('Moopgicians', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['lnt'], default=1)
    outreach = models.PositiveSmallIntegerField('OUTreach', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['outreach'], default=1)
    paparaunchy = models.PositiveSmallIntegerField('PapaRaunchy', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['paparaunchy'], default=1)
    playshops = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['playshops'], default=1)
    please = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['please'], default=1)
    road_warriors = models.PositiveSmallIntegerField('Road Warriors', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['road_warriors'], default=1)
    sales = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['sales'], default=1)
    swag = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['swag'], default=1)
    teleportus = models.PositiveSmallIntegerField('TeleportUs', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['teleportus'], default=1)
    ticketing = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['ticketing'], default=1)
    waldos = models.PositiveSmallIntegerField(null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['waldos'], default=1)
    wolf_pack=  models.PositiveSmallIntegerField('Wolf Pack', null=True, choices=RATING_CHOICES, help_text=TEAM_DESCRIPTION_DICT['wolf_pack'], default=1)
   
    def __iter__(self):
        
        for field_name in self._meta.get_all_field_names():
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)
            
    def __str__(self):
        return self.volunteer.first_name + " " + self.volunteer.last_name
        
#    def __init__(self):
#        super(Preferences2015, self).__init__()
#        for this_team in Team.objects.all():
#            ratings = Rating(volunteer_preferences= self, team= this_team)
            #ratings.save()
'''            
            

