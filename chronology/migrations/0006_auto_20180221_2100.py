# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0005_auto_20180221_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='s_in_charge',
            field=models.ForeignKey(blank=True, null=True, to='chronology.Manager', db_column='s_in_charge'),
        ),
    ]
