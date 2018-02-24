# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0014_auto_20180221_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_num',
            field=models.CharField(null=True, db_column='part_num', blank=True, max_length=45, default='1'),
        ),
    ]
