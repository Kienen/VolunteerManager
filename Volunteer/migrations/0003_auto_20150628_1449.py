# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0002_auto_20150628_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name']},
        ),
    ]
