# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0009_auto_20180221_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='part',
        ),
        migrations.AddField(
            model_name='part',
            name='part_num',
            field=models.CharField(max_length=45, db_column='part_num', default='1'),
        ),
    ]
