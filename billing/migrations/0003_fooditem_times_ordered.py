# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20150607_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='times_ordered',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
