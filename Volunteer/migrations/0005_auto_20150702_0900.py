# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0004_auto_20150702_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
