# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0008_auto_20150706_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(help_text=b"'999-999-9999'", max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\d{3}-\\d{3}-\\d{4}x?\\d{0,5}$', message=b"Phone number must be entered in the format: '999-999-9999x123'. ")]),
            preserve_default=True,
        ),
    ]
