# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(max_length=10)),
                ('product_type', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=30)),
                ('unit_price', models.IntegerField(default=0)),
                ('unit_available', models.IntegerField(default=0)),
                ('product_details', models.CharField(max_length=2000)),
                ('store_owns', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_no', models.IntegerField(default=0)),
                ('purchased_products', models.CharField(max_length=2000)),
                ('total_purchased_ammount', models.IntegerField(default=0)),
                ('purchased_date', models.DateTimeField(verbose_name=b'date purchased')),
                ('purchased_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30)),
                ('user_review', models.CharField(max_length=2000)),
                ('user_rating', models.IntegerField(default=0)),
                ('product', models.ForeignKey(to='cycleoholic.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=100)),
                ('sells_no', models.IntegerField(default=0)),
                ('sold_products', models.CharField(max_length=2000)),
                ('total_sold_ammount', models.IntegerField(default=0)),
                ('sells_date', models.DateTimeField(verbose_name=b'date sold')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sell',
            name='seller',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_from',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
    ]
