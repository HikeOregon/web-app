# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_trailimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrailImages',
            new_name='TrailImage',
        ),
    ]