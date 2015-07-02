# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0003_auto_20150628_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteer',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='team',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='limbo',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='FB_user_name',
            field=models.CharField(help_text=b'(http://www.facebook.com/--->USER NAME<--)', max_length=30, verbose_name=b'Facebook User Name', blank=True),
            preserve_default=True,
        ),
    ]
