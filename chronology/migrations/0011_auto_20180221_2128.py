# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0010_auto_20180221_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='p_in_charge_sub',
            field=models.ForeignKey(null=True, to='chronology.Manager', db_column='p_in_charge_sub', related_name='p_in_charge_sub', blank=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='p_in_charge',
            field=models.ForeignKey(null=True, to='chronology.Manager', db_column='p_in_charge', related_name='p_in_charge', blank=True),
        ),
    ]
