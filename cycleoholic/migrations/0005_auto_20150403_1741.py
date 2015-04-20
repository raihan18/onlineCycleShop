# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cycleoholic', '0004_auto_20150403_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_type', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='store',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='store_owns',
            field=models.ForeignKey(to='cycleoholic.Client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchased_from',
            field=models.ForeignKey(to='cycleoholic.Client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sell',
            name='seller',
            field=models.ForeignKey(to='cycleoholic.Client'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
