# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.CharField(default='here@ghere.com', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='approved_team',
            field=models.ForeignKey(to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
    ]
