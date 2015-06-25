# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0008_auto_20150619_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
