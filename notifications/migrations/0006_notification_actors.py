# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 09:01
from __future__ import unicode_literals

from django.db import migrations
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notifications', '0005_auto_20160504_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='actors',
            field=gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk')),
        ),
    ]
