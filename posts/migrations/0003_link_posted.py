# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20151101_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
