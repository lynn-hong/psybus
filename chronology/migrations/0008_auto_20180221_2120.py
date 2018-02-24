# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0007_auto_20180221_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='s_in_charge',
        ),
        migrations.AddField(
            model_name='part',
            name='p_in_charge',
            field=models.ForeignKey(to='chronology.Manager', blank=True, null=True, db_column='p_in_charge'),
        ),
    ]
