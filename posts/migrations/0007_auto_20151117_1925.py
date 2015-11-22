# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='lft',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='link',
            field=models.ForeignKey(to='posts.Link', default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(to='posts.Comment', null=True, related_name='children', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rght',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='tree_id',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
    ]
