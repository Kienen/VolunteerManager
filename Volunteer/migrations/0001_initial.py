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
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('budget', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=254, blank=True)),
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
                ('email', models.CharField(max_length=30)),
                ('playa_name', models.CharField(max_length=30, blank=True)),
                ('birthdate', models.DateField(help_text=b'mm/dd/yyyy', verbose_name=b'Birth Date')),
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
                ('ass', models.BooleanField(default=False, help_text=b"Some teams will be choosing the most dedicated, experienced volunteers to train as assistants to the leads. These super volunteers will receive more training and more responsibility. Not everyone is cut out for this position, but we're looking for the best of the best.", verbose_name=b'Are you interested in taking on more responsibility than most volunteers to make your department run smoothly and YOUtopia better than ever?')),
                ('avail_tu', models.BooleanField(default=True, verbose_name=b'Tuesday, October 13th')),
                ('avail_w', models.BooleanField(default=True, verbose_name=b'Wednesday, October 14st')),
                ('avail_th', models.BooleanField(default=True, verbose_name=b'Thursday, October 15nd')),
                ('avail_f', models.BooleanField(default=True, verbose_name=b'Friday, October 16th')),
                ('avail_sa', models.BooleanField(default=True, verbose_name=b'Saturday, October 17th')),
                ('avail_su', models.BooleanField(default=True, verbose_name=b'Sunday, October 18th')),
                ('avail_m', models.BooleanField(default=True, verbose_name=b'Monday, October 19th')),
                ('approved', models.BooleanField(default=False, help_text=b"Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests.", verbose_name=b'Have you already been selected to be part of a team?')),
                ('approved_by', models.CharField(max_length=30, blank=True)),
                ('has_ticket', models.BooleanField(default=False)),
                ('scheduled', models.BooleanField(default=False)),
                ('volunteer_rating', models.PositiveSmallIntegerField(null=True)),
                ('notes', models.CharField(max_length=254, null=True)),
                ('ratings', models.ManyToManyField(related_name='ratings', through='Volunteer.Rating', to='Volunteer.Team')),
                ('suggested_team', models.ForeignKey(related_name='suggested_team', blank=True, to='Volunteer.Team', null=True)),
                ('team', models.ForeignKey(related_name='team', blank=True, to='Volunteer.Team', null=True)),
                ('user', models.OneToOneField(related_name='profile', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='team',
            field=models.ForeignKey(to='Volunteer.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='volunteer',
            field=models.ForeignKey(to='Volunteer.Volunteer'),
            preserve_default=True,
        ),
    ]
