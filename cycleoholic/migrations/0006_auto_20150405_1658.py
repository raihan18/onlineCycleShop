# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cycleoholic', '0005_auto_20150403_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_address', models.CharField(max_length=200)),
                ('store_contact', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='store_owns',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchased_from',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sell',
            name='seller',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
