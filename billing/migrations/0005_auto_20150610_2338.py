# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20150610_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('category', models.CharField(max_length=32, choices=[('vegtables', 'vegtables'), ('groceries', 'groceries'), ('gas', 'gas'), ('non-veg', 'non-veg'), ('others', 'others'), ('misc', 'misc'), ('dairy', 'dairy')])),
                ('price', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodsBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('when', models.DateTimeField()),
                ('total', models.FloatField()),
                ('merchant', models.CharField(blank=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodsBillInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.FloatField(default=0)),
                ('bill', models.ForeignKey(to='billing.GoodsBill')),
                ('item', models.ForeignKey(to='billing.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='goodsexpense',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='goodsexpense',
            name='bill',
        ),
        migrations.DeleteModel(
            name='GoodsExpense',
        ),
        migrations.DeleteModel(
            name='GoodsExpenseBill',
        ),
    ]
