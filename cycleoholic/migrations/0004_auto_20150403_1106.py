# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycleoholic', '0003_auto_20150403_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='store_owns',
            field=models.ForeignKey(to='cycleoholic.Store'),
            preserve_default=True,
        ),
    ]
