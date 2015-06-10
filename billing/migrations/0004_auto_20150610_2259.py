# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_fooditem_times_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsexpense',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goodsexpense',
            name='category',
            field=models.CharField(max_length=32, choices=[('vegtables', 'vegtables'), ('groceries', 'groceries'), ('gas', 'gas'), ('non-veg', 'non-veg'), ('others', 'others'), ('misc', 'misc'), ('dairy', 'dairy')]),
        ),
        migrations.AlterField(
            model_name='goodsexpense',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='goodsexpense',
            unique_together=set([('bill', 'name')]),
        ),
    ]
