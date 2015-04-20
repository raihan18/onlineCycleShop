# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cycleoholic', '0006_auto_20150405_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='store_owns',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
