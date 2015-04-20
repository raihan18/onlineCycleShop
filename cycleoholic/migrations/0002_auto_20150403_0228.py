# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycleoholic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_no',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='sells_no',
        ),
    ]
