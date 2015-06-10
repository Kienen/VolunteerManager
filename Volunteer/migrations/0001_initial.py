# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences2015',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avail_tu', models.BooleanField(default=True, verbose_name=b'Tuesday, October 20th')),
                ('avail_w', models.BooleanField(default=True, verbose_name=b'Wednesday, October 21st')),
                ('avail_th', models.BooleanField(default=True, verbose_name=b'Thursday, October 22nd')),
                ('avail_f', models.BooleanField(default=True, verbose_name=b'Friday, October 23rd')),
                ('avail_sa', models.BooleanField(default=True, verbose_name=b'Saturday, October 24th')),
                ('avail_su', models.BooleanField(default=True, verbose_name=b'Sunday, October 25th')),
                ('avail_m', models.BooleanField(default=True, verbose_name=b'Monday, October 26th')),
                ('ass', models.BooleanField(default=False, help_text=b"Some teams will be choosing the most dedicated, experienced volunteers to train as assistants to the leads. These super volunteers will receive more training and more responsibility. Not everyone is cut out for this position, but we're looking for the best of the best.", verbose_name=b'Are you interested in taking on more responsibility than most volunteers to make your department run smoothly and YOUtopia better than ever?')),
                ('approved', models.BooleanField(default=False, help_text=b"Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests. If you have already confirmed with your department lead that you will work with this team, please fill in this box then skip to the next section.", verbose_name=b'Have you already been selected to be part of a team?')),
                ('approved_by', models.CharField(max_length=30, blank=True)),
                ('ada', models.PositiveSmallIntegerField(default=1, help_text=b'Mobility Assistance', null=True, verbose_name=b'ADA', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('art_curation', models.PositiveSmallIntegerField(default=1, help_text=b'Coordinating with local artists to keep YOUtopia weird.', null=True, verbose_name=b'Art Curation', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('center_camp', models.PositiveSmallIntegerField(default=1, help_text=b'Whether it\xe2\x80\x99s managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.', null=True, verbose_name=b'Center Camp', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('city_planning', models.PositiveSmallIntegerField(default=1, help_text=b"Whether it's managing the stage and myriad activities at Center Camp or maintaining sacred space at the Temple, this crew helps maintain spaces where each and every YOUtopian can gift their participation.", null=True, verbose_name=b'City Planning', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('commissary', models.PositiveSmallIntegerField(default=1, help_text=b"So you're hungry, are you? The good people at the Commissary make sure the event crew can stay fat and sassy by keeping them fed, because we all love to keep it sassy.", null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('dispatch', models.PositiveSmallIntegerField(default=1, help_text=b'Dispatch are the masters of radio communication. They keep our airwaves clear and help distribute information. Over.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('dispensary', models.PositiveSmallIntegerField(default=1, help_text=b'I got what you want. I got what you need. The dispensary maintains YOUtopia supplies and equipment and makes sure each department is set up for success.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('fire', models.PositiveSmallIntegerField(default=1, help_text=b'Keeping us safe from lighting ourselves, others, and anything other than approved art and performance on fire, Fire Safety knows to keep the fire alive at the event. They\xe2\x80\x99re also the hard working crew that facilitates safety classes at the event to give you your first opportunity (or perhaps your 7,456,398 opportunity) to light up your fire.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('gate', models.PositiveSmallIntegerField(default=1, help_text=b'These are the people who make sure your entrance into the event is a smooth ride. They check that you know about the rules concerning what you can bring into the event (No Glass or Firewood please!), make sure you have your ticket, and work closely with Security to protect the perimeter of the event.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('greeters', models.PositiveSmallIntegerField(default=1, help_text=b'These are the folks that welcome participants with open arms into YOUtopia, while making sure you know where you\xe2\x80\x99re going, providing answers to your questions about the event, and giving you a good hug (or a good spanking) at your request. ', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('lnt', models.PositiveSmallIntegerField(default=1, help_text=b'The Moopgician crew makes sure that participants leave a pristine location when the event is over. They help educate participants on having the least ecological impact and \xe2\x80\x9cPack It In, Pack It Out\xe2\x80\x9d principles. They may also sometimes be found leading scavenger hunts and games.', null=True, verbose_name=b'Moopgicians', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('outreach', models.PositiveSmallIntegerField(default=1, help_text=b"Masters of media relations and information dissemination, the OUTreach team knows what's shakin' and keeps the party rockin'.", null=True, verbose_name=b'OUTreach', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('paparaunchy', models.PositiveSmallIntegerField(default=1, help_text=b"If there's a totally righteous party in the forest, and no one is there to see it, did it really happen? Our media crew documents building the city from the early planning meetings to cleaning up on the way out.", null=True, verbose_name=b'PapaRaunchy', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('playshops', models.PositiveSmallIntegerField(default=1, help_text=b'Aptly titled because they\xe2\x80\x99re all about play!, Playshops provide activities like that early sunrise yoga to get a jumpstart to your day, a lesson on how to plant your very own unicorn, or a open dialogue about what it means to be a burner. Playshops & Performances Support play cupid, matchmaking Theme Camps with open space to host with those seeking a space to express their creativity. As wide-ranging as the imagination, they sometimes need a little support with those yoga mats or unicorn seeds.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('please', models.PositiveSmallIntegerField(default=1, help_text=b'The Please Department supports the service of all other YOUtopia volunteer crews. They\xe2\x80\x99re an elite strike force whose mission is to ensure members of the event team take care of themselves by delivering food, snacks, extra help, and overall fun. When not caretaking for other departments, they can usually be found instigating shenanigans somewhere in the event.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('road_warriors', models.PositiveSmallIntegerField(default=1, help_text=b"The Road Warriors make sure we can all fit comfortably in the event. Working closely with City Planning, Road Warriors have a good handle on mapping out how exactly to fit all the cars, RVs, and other vehicles into the event with style and grace. They're looking for experienced volunteers who work hard and play hard.", null=True, verbose_name=b'Road Warriors', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('sales', models.PositiveSmallIntegerField(default=1, help_text=b'Slinging coffee and ice on the mountain, the Sales crew wakes us up and keeps things cool, and donates the proceeds to the tribe.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('swag', models.PositiveSmallIntegerField(default=1, help_text=b'Make 2015 memorable for all our volunteers with awesome gear and nifty collectibles.', null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('teleportus', models.PositiveSmallIntegerField(default=1, help_text=b'Facilitating shuttles and art cars to help cruise participants around YOUtopia in style, TeleportUs crew keeps it movin.', null=True, verbose_name=b'TeleportUs', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('ticketing', models.PositiveSmallIntegerField(default=1, help_text=b"They're making a list and checking it twice. These volunteers keep the line cruising.", null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('waldos', models.PositiveSmallIntegerField(default=1, help_text=b"The Waldos keep an eagle eye open for uninvited guestss. They maintain a drag net to keep the perimeter secure and work closely with security to ensure anyone who isn't supposed to be at the event isn't at the event.", null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('wolf_pack', models.PositiveSmallIntegerField(default=1, help_text=b'Abiding by their motto, "First To Come, Last To Pull Out," the Wolf Pack are a die hard crew. Literally building the event from the ground up, this crew sees to it that the infrastructure for our fair YOUtopian city is in place for the event. They are also responsible for disassembling everything at the conclusion of the event so our city leaves no trace.', null=True, verbose_name=b'Wolf Pack', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('budget', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('playa_name', models.CharField(max_length=30, blank=True)),
                ('birthdate', models.DateField(verbose_name=b'Birth Date')),
                ('phone', models.CharField(help_text=b"'999-999-9999'", max_length=20)),
                ('emergency_contact', models.CharField(max_length=30)),
                ('emergency_phone', models.CharField(help_text=b"'999-999-999'", max_length=20)),
                ('FB_user_name', models.CharField(help_text=b'(i.e. http://www.facebook.com/"YOU")', max_length=30, verbose_name=b'Facebook User Name', blank=True)),
                ('diet', models.CharField(default=b'Omnivore', help_text=b'Please choose the answer that *best* fits your dietary lifestyle.', max_length=30, verbose_name=b'Dietary Preference', choices=[(b'Omnivore', b'Omnivore - I like everything including Meat'), (b'Vegetarian', b"Vegetarian - I don't eat any meat"), (b'Vegan', b"Vegan - I don't eat any animal products!")])),
                ('diet_restriction', models.CharField(help_text=b"Please list any food allergies. We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs.", max_length=254, verbose_name=b'Specific dietary restriction', blank=True)),
                ('disability', models.CharField(max_length=254, verbose_name=b'Do you have any health or disability issues we should be aware of?', blank=True)),
                ('attended_BM', models.BooleanField(default=False, verbose_name=b'Have you attended a Burning Man event before?')),
                ('v_YOUtopia', models.BooleanField(default=False, verbose_name=b'Have you volunteered with YOUtopia before?')),
                ('vexp_YOUtopia', models.CharField(max_length=254, verbose_name=b'If YES, which teams have you worked with?', blank=True)),
                ('v_other', models.BooleanField(default=False, verbose_name=b'Have you volunteered with any other festivals or events before? ')),
                ('vexp_other', models.CharField(max_length=254, verbose_name=b'If YES, please specify.', blank=True)),
                ('super_powers', models.CharField(help_text=b'What special super powers or skills you have? What skills would you like to learn more about?', max_length=254, verbose_name=b'Super Powers', blank=True)),
                ('jokes', models.CharField(help_text=b'How do you kill a circus? Go for the juggler.', max_length=254, verbose_name=b'Questions? Comments? Favorite Joke?', blank=True)),
                ('suggested_team', models.CharField(max_length=30, null=True)),
                ('has_ticket', models.BooleanField(default=False)),
                ('scheduled', models.BooleanField(default=False)),
                ('rating', models.PositiveSmallIntegerField(null=True)),
                ('notes', models.CharField(max_length=254, null=True)),
                ('team', models.ForeignKey(to='Volunteer.Team', null=True)),
                ('user', models.OneToOneField(related_name='profile', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='preferences2015',
            name='approved_team',
            field=models.ForeignKey(to='Volunteer.Team', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='preferences2015',
            name='volunteer',
            field=models.OneToOneField(null=True, to='Volunteer.Volunteer'),
            preserve_default=True,
        ),
    ]
