# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='super_powers',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='notes',
            field=models.CharField(max_length=254, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='suggested_team',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='team',
            field=models.ForeignKey(to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
    ]
