# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('total', models.FloatField()),
                ('table', models.CharField(choices=[('1', 'TABLE 1'), ('2', 'TABLE 2'), ('3', 'TABLE 3'), ('4', 'TABLE 4'), ('5', 'TABLE 5'), ('6', 'TABLE 6')], max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.CharField(choices=[('VEG DRY', 'VEG DRY'), ('NON VEG DRY', 'NON VEG DRY'), ('VEG TIFFIN', 'VEG TIFFIN'), ('NON VEG TIFFIN', 'NON VEG TIFFIN'), ('DESSERTS', 'DESSERTS'), ('COOL DRINKS', 'COOL DRINKS')], max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('category', models.CharField(choices=[('vegtables', 'vegtables'), ('groceries', 'groceries'), ('gas', 'gas'), ('non-veg', 'non-veg'), ('others', 'others'), ('misc', 'misc')], max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodsExpenseBill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('total', models.FloatField()),
                ('merchant', models.CharField(blank=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
