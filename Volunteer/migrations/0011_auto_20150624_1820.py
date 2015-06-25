# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0010_auto_20150620_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_f',
            field=models.BooleanField(default=True, verbose_name=b'Friday, October 16th'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_m',
            field=models.BooleanField(default=True, verbose_name=b'Monday, October 19th'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_sa',
            field=models.BooleanField(default=True, verbose_name=b'Saturday, October 17th'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_su',
            field=models.BooleanField(default=True, verbose_name=b'Sunday, October 18th'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_th',
            field=models.BooleanField(default=True, verbose_name=b'Thursday, October 15nd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_tu',
            field=models.BooleanField(default=True, verbose_name=b'Tuesday, October 13th'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferences2015',
            name='avail_w',
            field=models.BooleanField(default=True, verbose_name=b'Wednesday, October 14st'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='suggested_team',
            field=models.ForeignKey(related_name='suggested_team', blank=True, to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='team',
            field=models.ForeignKey(related_name='team', blank=True, to='Volunteer.Team', null=True),
            preserve_default=True,
        ),
    ]
