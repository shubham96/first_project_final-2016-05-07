# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0005_auto_20160404_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='stud_id',
        ),
    ]