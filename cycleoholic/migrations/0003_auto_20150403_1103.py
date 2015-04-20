# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cycleoholic', '0002_auto_20150403_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
