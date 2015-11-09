# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_link_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
