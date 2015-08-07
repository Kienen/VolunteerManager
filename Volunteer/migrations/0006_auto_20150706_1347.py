# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0005_auto_20150702_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='notes',
            field=models.CharField(default='', max_length=254, blank=True),
            preserve_default=False,
        ),
    ]
