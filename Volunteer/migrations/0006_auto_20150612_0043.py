# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0005_auto_20150610_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences2015',
            name='approved',
            field=models.BooleanField(default=False, help_text=b"Some department heads are recruiting team members in advance. If you haven't already been recruited, not to fret! We will help place you on a team that fits your skills and interests.", verbose_name=b'Have you already been selected to be part of a team?'),
            preserve_default=True,
        ),
    ]
