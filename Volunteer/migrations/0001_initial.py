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
                ('avail_tu', models.BooleanField(default=True)),
                ('avail_w', models.BooleanField(default=True)),
                ('avail_th', models.BooleanField(default=True)),
                ('avail_f', models.BooleanField(default=True)),
                ('avail_sa', models.BooleanField(default=True)),
                ('avail_su', models.BooleanField(default=True)),
                ('avail_m', models.BooleanField(default=True)),
                ('ass', models.BooleanField(default=False)),
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
                ('playa_name', models.CharField(max_length=30, null=True)),
                ('birthdate', models.DateTimeField(verbose_name=b'Birth Date')),
                ('phone', models.CharField(help_text=b"'999-999-9999'", max_length=20)),
                ('emergency_contact', models.CharField(max_length=30)),
                ('emergency_phone', models.CharField(help_text=b"'999-999-999'", max_length=20)),
                ('FB_user_name', models.CharField(help_text=b'(i.e. http://www.facebook.com/"YOU")', max_length=30, null=True, verbose_name=b'Facebook User Name')),
                ('diet', models.IntegerField(default=1, help_text=b'Please choose the answer that *best* fits your dietary lifestyle.', verbose_name=b'Dietary Preference', choices=[(1, b'Omnivore - I like everything including Meat'), (2, b"Vegetarian - I don't eat any meat"), (3, b'Vegan - I don\t eat any animal products!')])),
                ('diet_restriction', models.CharField(help_text=b"Please list any food allergies. We encourage everyone to practice Radical Self-Reliance and provide food for themselves as we cannot guarantee our ability to accommodate everyone's dietary needs.", max_length=254, null=True, verbose_name=b'Specific dietary restriction')),
                ('disability', models.CharField(max_length=254, verbose_name=b'Do you have any health or disability issues we should be aware of?')),
                ('attended_BM', models.BooleanField(default=False, verbose_name=b'Have you attended a Burning Man event before?')),
                ('v_YOUtopia', models.BooleanField(default=False, verbose_name=b'Have you volunteered with YOUtopia before?')),
                ('vexp_YOUtopia', models.CharField(max_length=254, null=True, verbose_name=b'If YES, which teams have you worked with?')),
                ('v_other', models.BooleanField(default=False, verbose_name=b'Have you volunteered with any other festivals or events before? ')),
                ('vexp_other', models.CharField(max_length=254, null=True, verbose_name=b'If YES, please specify.')),
                ('super_powers', models.CharField(help_text=b'What special super powers or skills you have? What skills would you like to learn more about?', max_length=254, null=True, verbose_name=b'Super Powers')),
                ('jokes', models.CharField(help_text=b'How do you kill a circus? Go for the juggler.', max_length=254, null=True, verbose_name=b'Questions? Comments? Favorite Joke?')),
                ('suggested_team', models.CharField(max_length=30, null=True)),
                ('has_ticket', models.BooleanField(default=False)),
                ('scheduled', models.BooleanField(default=False)),
                ('rating', models.PositiveSmallIntegerField(null=True)),
                ('notes', models.CharField(max_length=254, null=True)),
                ('team', models.ForeignKey(to='Volunteer.Team', null=True)),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='preferences2015',
            name='volunteer',
            field=models.OneToOneField(to='Volunteer.Volunteer'),
            preserve_default=True,
        ),
    ]
