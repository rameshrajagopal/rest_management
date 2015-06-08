# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('bill', models.ForeignKey(to='billing.Bill')),
                ('item', models.ForeignKey(to='billing.FoodItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodsExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('category', models.CharField(choices=[('vegtables', 'vegtables'), ('groceries', 'groceries'), ('gas', 'gas'), ('non-veg', 'non-veg'), ('others', 'others'), ('misc', 'misc')], max_length=32)),
                ('quantity', models.FloatField()),
                ('bill', models.ForeignKey(to='billing.GoodsExpenseBill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]
