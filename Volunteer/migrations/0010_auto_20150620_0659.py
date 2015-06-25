# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0009_auto_20150619_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='suggested_team',
            field=models.ForeignKey(related_name='suggested_team', to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='team',
            field=models.ForeignKey(related_name='team', to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
    ]
