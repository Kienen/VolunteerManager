# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0006_auto_20150612_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.PositiveSmallIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='birthdate',
            field=models.DateField(help_text=b'mm/dd/yyyy', verbose_name=b'Birth Date'),
            preserve_default=True,
        ),
    ]
