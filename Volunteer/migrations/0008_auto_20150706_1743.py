# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0007_auto_20150706_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='ass',
            field=models.BooleanField(default=False, help_text=b"Some teams will be choosing the most dedicated, experienced volunteers to train as assistants to the leads. These super volunteers will receive more training and more responsibility. Not everyone is cut out for this position, but we're looking for the best of the best.", verbose_name=b'Super Volunteer'),
            preserve_default=True,
        ),
    ]
