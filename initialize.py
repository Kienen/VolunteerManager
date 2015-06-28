# -*- coding: utf-8 -*-
from Volunteer.models import Team
TEAMS = {'ADA': 5,
        'Center Camp': 5,
        'City Planning': 12,
        'Commissary': 35,
        'Dispatch': 5,
        'Dispensary': 8,
        'Fire': 13,
        'Gate': 32,
        'Greeters': 10,
        'LNT': 23,
        'Outreach': 11,
        'Paparaunchy': 5,
        'Playshops': 11,
        'Please': 38,
        'Road Warriors': 44,
        'Sales': 5,
        'Swag': 5,
        'Teleportus ': 38,
        'ticketing ': 16,
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
        'Road_warriors': "The Road Warriors make sure we can all fit comfortably in the event. Working closely with City Planning, Road Warriors have a good handle on mapping out how exactly to fit all the cars, RVs, and other vehicles into the event with style and grace. They're looking for experienced volunteers who work hard and play hard.",
        'Sales': "Slinging coffee and ice on the mountain, the Sales crew wakes us up and keeps things cool, and donates the proceeds to the tribe.",
        'Swag': "Make 2015 memorable for all our volunteers with awesome gear and nifty collectibles.",
        'Teleportus ': "Facilitating shuttles and art cars to help cruise participants around YOUtopia in style, TeleportUs crew keeps it movin.",
        'ticketing ': "They're making a list and checking it twice. These volunteers keep the line cruising.",
        'Waldos': "The Waldos keep an eagle eye open for uninvited guestss. They maintain a drag net to keep the perimeter secure and work closely with security to ensure anyone who isn't supposed to be at the event isn't at the event.",  
        'Wolf Pack': "Abiding by their motto, \"First To Come, Last To Pull Out,\" the Wolf Pack are a die hard crew. Literally building the event from the ground up, this crew sees to it that the infrastructure for our fair YOUtopian city is in place for the event. They are also responsible for disassembling everything at the conclusion of the event so our city leaves no trace.",
                      }
                      
for team_name, budget in teams:
    team = Team(budget= budget, name= team_name, description = TEAM_DESCRIPTION_DICT[team_name])
    team.save
    
    